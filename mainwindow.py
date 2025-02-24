import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox
from PySide6.QtCore import Signal, Qt

from AddFactoryDialog import AddFactoryDialog
from PercentDelegate import PercentDelegate
from ui_form import Ui_MainWindow

class MainWindow(QMainWindow):

    # Señales para notificar la adición y eliminación de filas
    rowAdded = Signal(int)
    rowRemoved = Signal(int)

    def __init__(self, parent=None):
        super().__init__(parent)

        # Setupeamos la interfaz gráfica
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Conectamos los botones de añadir y eliminar fábrica con su funcionamiento
        self.ui.btn_add.clicked.connect(self.open_add_factory_dialog)
        self.ui.btn_del.clicked.connect(self.delete_factory)

        # Mostramos un mensaje en la barra de estado por defecto
        self.ui.statusbar.showMessage("Puedes pasar el mouse sobre las cabeceras de las columnas para una mejor descripción!")

        # Variable para evitar recursividad al actualizar los items, ya que queremos
        # que al modificar algun porcentaje se actualicen todos los cálculos.

        # Esto es muy importante para evitar bucles infinitos
        self._updating = False

        # Si se modifica algún item de la tabla, se llama a la función on_item_changed
        self.ui.table.itemChanged.connect(self.on_item_changed)

        # Se asigna el delegate para las columnas de P(Fábrica) (índice 1) y P(D|Fábrica) (índice 2)
        # para que se muestren y editen los porcentajes de manera más amigable
        self.percent_delegate = PercentDelegate(self)
        self.ui.table.setItemDelegateForColumn(1, self.percent_delegate)
        self.ui.table.setItemDelegateForColumn(2, self.percent_delegate)

        # Configurar tooltips en los encabezados de la tabla
        self.set_header_tooltips()

    # Función para asignar tooltips a los encabezados de la tabla
    def set_header_tooltips(self):
        headers = [
            "Nombre de la fábrica\n(Identificador de la instalación)",
            "P(Fábrica)\n(Porcentaje de producción asignado a esta fábrica; la suma total debe ser 100% para realizar los cálculos)",
            "P(D|Fábrica)\n(Porcentaje de piezas defectuosas en esta fábrica)",
            "P(ND|Fábrica)\n(Porcentaje de piezas sin defecto en esta fábrica)",
            "P(Fábrica|D)\n(Probabilidad de que una pieza defectuosa provenga de esta fábrica)",
            "P(Fábrica|ND)\n(Probabilidad de que una pieza sin defecto provenga de esta fábrica)"
        ]

        for i, tip in enumerate(headers):
            header_item = self.ui.table.horizontalHeaderItem(i)
            if header_item:
                header_item.setToolTip(tip)

    # Función para abrir el diálogo de añadir fábrica
    def open_add_factory_dialog(self):
        add_factory_dialog = AddFactoryDialog()
        add_factory_dialog.factoryAdded.connect(self.add_factory)
        add_factory_dialog.exec()

    # Función para añadir una fábrica a la tabla
    def add_factory(self, name, prod, defect):
        row_count = self.ui.table.rowCount()
        self.ui.table.insertRow(row_count)

        # Crear los items de la fila con los datos de la fábrica
        item_name = QTableWidgetItem(name)
        item_prod = QTableWidgetItem(str(prod) + "%")
        item_defect = QTableWidgetItem(str(defect) + "%")

        self.ui.table.setItem(row_count, 0, item_name)
        self.ui.table.setItem(row_count, 1, item_prod)
        self.ui.table.setItem(row_count, 2, item_defect)

        # Para las columnas 3, 4 y 5 se crean items de solo lectura con texto vacío (inicialmente)
        for col in range(3, 6):
            item = QTableWidgetItem("")

            # Se deshabilita la edición de los items
            item.setFlags(item.flags() & ~Qt.ItemIsEditable)
            self.ui.table.setItem(row_count, col, item)

        # Emitir la señal de fila añadida y actualizar los cálculos
        self.rowAdded.emit(row_count)
        self.update_calculations()

    # Función para eliminar una fábrica de la tabla
    def delete_factory(self):
        selected_row = self.ui.table.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "Error", "Selecciona una fábrica para eliminar.")
            return

        reply = QMessageBox.question(
            self, "Confirmar", "¿Deseas eliminar esta fábrica?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            self.ui.table.removeRow(selected_row)
            self.rowRemoved.emit(selected_row)
            self.update_calculations()

    def on_item_changed(self, item):

        # Evitar recursividad al actualizar los items
        if self._updating:
            return

        # Si se modifica P(Fábrica) (columna 1) o P(D|Fábrica) (columna 2), se recalculan los valores
        # Esto es para no actualizar los datos innecesariamente en la columna de nombres
        if item.column() in (1, 2):
            self.update_calculations()

    # Este es el metodo más importante, ya que es el que se encarga de realizar los cálculos!
    def update_calculations(self):

        """
        Recalcula los valores basados en el teorema de Bayes para cada fila,
        siempre y cuando la suma de los porcentajes en la columna P(Fábrica) sea 100%.
        Si no es así, se muestra un aviso en la barra de estado.
        """

        # Habilitamos la edición de los items
        self._updating = True
        rows = self.ui.table.rowCount()
        total_pF = 0.0

        # Sumar los porcentajes de la columna P(Fábrica) (columna 1)
        for i in range(rows):
            item_pF = self.ui.table.item(i, 1)
            if item_pF is not None:
                try:
                    value = float(item_pF.text().replace("%", "").strip())
                except ValueError:
                    value = 0.0
                total_pF += value

        # Verificar la suma total
        # Si la suma total no es 100%, se muestra un mensaje en la barra de estado
        # y se limpian las columnas calculadas
        if abs(total_pF - 100) > 1e-6:
            self.ui.statusbar.showMessage("La suma de P(Fábrica) debe ser 100% para realizar los cálculos!")

            # Se limpian las columnas calculadas
            for i in range(rows):
                for col in range(3, 6):
                    item = self.ui.table.item(i, col)
                    if item is not None:
                        item.setText("")
                    else:
                        new_item = QTableWidgetItem("")
                        new_item.setFlags(new_item.flags() & ~Qt.ItemIsEditable)
                        self.ui.table.setItem(i, col, new_item)

            # Se deshabilita la edición de los items
            self._updating = False

            return
        else:
            self.ui.statusbar.clearMessage()

        # Si la suma total es 100%, se procede a realizar los cálculos!

        # Calcular el P(D) global: suma de pF * p(D|F) (trabajando en escala 0-1)
        P_D = 0.0
        for i in range(rows):
            try:
                pF = float(self.ui.table.item(i, 1).text().replace("%", "").strip()) / 100
            except (ValueError, AttributeError):
                pF = 0.0
            try:
                pD = float(self.ui.table.item(i, 2).text().replace("%", "").strip()) / 100
            except (ValueError, AttributeError):
                pD = 0.0
            P_D += pF * pD
        P_ND = 1 - P_D

        # Para cada fila, calcular:
        # - P(ND|F) = (1 - p(D|F)) * 100
        # - P(F|D) = (pF * p(D|F) / P(D)) * 100   (si P(D) > 0)
        # - P(F|ND) = (pF * (1 - p(D|F)) / P(ND)) * 100   (si P(ND) > 0)
        for i in range(rows):
            try:
                pF = float(self.ui.table.item(i, 1).text().replace("%", "").strip()) / 100
            except (ValueError, AttributeError):
                pF = 0.0
            try:
                pD = float(self.ui.table.item(i, 2).text().replace("%", "").strip()) / 100
            except (ValueError, AttributeError):
                pD = 0.0

            pND_F = (1 - pD) * 100
            pF_D = (pF * pD / P_D * 100) if P_D > 0 else 0
            pF_ND = (pF * (1 - pD) / P_ND * 100) if P_ND > 0 else 0

            text_pND_F = f"{pND_F:.2f}%"
            text_pF_D = f"{pF_D:.2f}%"
            text_pF_ND = f"{pF_ND:.2f}%"

            # Actualizar los items de las columnas calculadas
            for col, text in zip(range(3, 6), [text_pND_F, text_pF_D, text_pF_ND]):
                item = self.ui.table.item(i, col)
                if item is None:
                    item = QTableWidgetItem(text)
                    item.setFlags(item.flags() & ~Qt.ItemIsEditable)
                    self.ui.table.setItem(i, col, item)
                else:
                    item.setText(text)

        # Deshabilitar la edición de los items
        self._updating = False


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
