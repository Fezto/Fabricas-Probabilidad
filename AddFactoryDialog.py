from PySide6.QtCore import Signal
from PySide6.QtWidgets import QDialog, QMessageBox

# Importar la clase generada por Qt Designer (ui_add_factory.py)
from ui_add_factory import Ui_AddFactory


class AddFactoryDialog(QDialog):

    # Señal que envía el nombre de la fábrica, P(Fábrica) y P(D|Fábrica)
    factoryAdded = Signal(str, float, float)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_AddFactory()
        self.ui.setupUi(self)
        self.ui.btn.clicked.connect(self.add_factory)

    def add_factory(self):
        name = self.ui.line_edit_name.text().strip()
        prod = self.ui.spin_box_prod.value()
        defect = self.ui.spin_box_def.value()

        if not name:
            QMessageBox.warning(self, "Error", "El nombre de la fábrica no puede estar vacío.")
            return

        # Emitir la señal con los datos de la fábrica a MainWindow
        self.factoryAdded.emit(name, prod, defect)
        self.accept()