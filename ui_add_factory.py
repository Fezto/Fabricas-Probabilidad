# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_factory.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpinBox,
    QVBoxLayout, QWidget)

class Ui_AddFactory(object):
    def setupUi(self, AddFactory):
        if not AddFactory.objectName():
            AddFactory.setObjectName(u"AddFactory")
        AddFactory.resize(393, 294)
        AddFactory.setMaximumSize(QSize(600, 16777215))
        self.layoutWidget = QWidget(AddFactory)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(11, 11, 371, 271))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_2.addWidget(self.label_4)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.line_edit_name = QLineEdit(self.layoutWidget)
        self.line_edit_name.setObjectName(u"line_edit_name")
        self.line_edit_name.setMaxLength(32767)
        self.line_edit_name.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.line_edit_name)

        self.spin_box_prod = QSpinBox(self.layoutWidget)
        self.spin_box_prod.setObjectName(u"spin_box_prod")
        self.spin_box_prod.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.spin_box_prod)

        self.spin_box_def = QSpinBox(self.layoutWidget)
        self.spin_box_def.setObjectName(u"spin_box_def")
        self.spin_box_def.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.spin_box_def)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.btn = QPushButton(self.layoutWidget)
        self.btn.setObjectName(u"btn")

        self.verticalLayout_3.addWidget(self.btn)

        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 4)
        self.verticalLayout_3.setStretch(2, 1)

        self.retranslateUi(AddFactory)

        QMetaObject.connectSlotsByName(AddFactory)
    # setupUi

    def retranslateUi(self, AddFactory):
        AddFactory.setWindowTitle(QCoreApplication.translate("AddFactory", u"Dialog", None))
        self.label_3.setText(QCoreApplication.translate("AddFactory", u"A\u00f1adir f\u00e1brica", None))
        self.label.setText(QCoreApplication.translate("AddFactory", u"Nombre: ", None))
        self.label_4.setText(QCoreApplication.translate("AddFactory", u"Porcentaje de producci\u00f3n", None))
        self.label_2.setText(QCoreApplication.translate("AddFactory", u"Probabilidad de producto defectuoso: ", None))
        self.line_edit_name.setInputMask("")
        self.line_edit_name.setText("")
        self.line_edit_name.setPlaceholderText("")
        self.spin_box_prod.setSuffix(QCoreApplication.translate("AddFactory", u"%", None))
        self.spin_box_def.setSuffix(QCoreApplication.translate("AddFactory", u"%", None))
        self.btn.setText(QCoreApplication.translate("AddFactory", u"\u00a1Agregar!", None))
    # retranslateUi

