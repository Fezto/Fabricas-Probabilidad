from PySide6.QtCore import Qt
from PySide6.QtGui import QIntValidator
from PySide6.QtWidgets import QStyledItemDelegate, QLineEdit

# Esta clase se encarga de crear un editor personalizado para las celdas de la tabla
# con el fin de que el usuario pueda ingresar porcentajes (números enteros entre 0 y 100)
# de manera más sencilla sin tener que escribir "%". También sirve para validar que lo que
# se ingrese sea siempre un número entero entre el 0 y el 100.

class PercentDelegate(QStyledItemDelegate):

    # Los delegados son clases que permiten personalizar la forma en que se editan y muestran los datos
    # Todos estos son métodos por defecto de QStyledItemDelegate, solo que se han sobrescrito
    # para adaptar el comportamiento del editor a nuestras necesidades.

    # Crear un editor personalizado para las celdas de la tabla
    def createEditor(self, parent, option, index):
        editor = QLineEdit(parent)
        validator = QIntValidator(0, 100, editor)
        editor.setValidator(validator)
        return editor

    # Establecer el texto del editor con el valor actual de la celda
    def setEditorData(self, editor, index):
        text = index.model().data(index, Qt.EditRole)
        if text:
            if text.endswith('%'):

                # Eliminar el "%" al final del texto si el usuario lo ingresó
                text = text[:-1]

            editor.setText(text)
        else:
            editor.setText("")

    # Establecer el valor de la celda con el texto ingresado en el editor
    def setModelData(self, editor, model, index):
        text = editor.text().strip()

        # Agregamos el "%" al final siempre programáticamente
        if not text.endswith('%'):
            text += '%'

        model.setData(index, text, Qt.EditRole)