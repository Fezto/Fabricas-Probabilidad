# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTabWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 400)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(800, 400))
        MainWindow.setMaximumSize(QSize(800, 400))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.horizontalLayout_6 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.tab_one = QTabWidget(self.centralwidget)
        self.tab_one.setObjectName(u"tab_one")
        self.tab_one_2 = QWidget()
        self.tab_one_2.setObjectName(u"tab_one_2")
        self.widget = QWidget(self.tab_one_2)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 20, 741, 271))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(25)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(15)
        self.label_2.setFont(font1)
        self.label_2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_2.setWordWrap(True)

        self.verticalLayout.addWidget(self.label_2)

        self.tab_one.addTab(self.tab_one_2, "")
        self.tab_all = QWidget()
        self.tab_all.setObjectName(u"tab_all")
        self.layoutWidget = QWidget(self.tab_all)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 751, 291))
        self.horizontalLayout_5 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.table = QTableWidget(self.layoutWidget)
        if (self.table.columnCount() < 6):
            self.table.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.table.setObjectName(u"table")
        sizePolicy1.setHeightForWidth(self.table.sizePolicy().hasHeightForWidth())
        self.table.setSizePolicy(sizePolicy1)
        self.table.setRowCount(0)
        self.table.setColumnCount(6)

        self.horizontalLayout_5.addWidget(self.table)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(15)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(10, -1, 0, 0)
        self.btn_add = QPushButton(self.layoutWidget)
        self.btn_add.setObjectName(u"btn_add")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_add.sizePolicy().hasHeightForWidth())
        self.btn_add.setSizePolicy(sizePolicy2)

        self.verticalLayout_6.addWidget(self.btn_add)

        self.btn_del = QPushButton(self.layoutWidget)
        self.btn_del.setObjectName(u"btn_del")
        sizePolicy2.setHeightForWidth(self.btn_del.sizePolicy().hasHeightForWidth())
        self.btn_del.setSizePolicy(sizePolicy2)

        self.verticalLayout_6.addWidget(self.btn_del)

        self.verticalLayout_6.setStretch(0, 3)
        self.verticalLayout_6.setStretch(1, 1)

        self.horizontalLayout_5.addLayout(self.verticalLayout_6)

        self.tab_one.addTab(self.tab_all, "")

        self.horizontalLayout_6.addWidget(self.tab_one)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 20))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setSizeGripEnabled(True)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tab_one.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Teorema de Bayes", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u00bfQu\u00e9 probabilidad hay...?", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Este proyecto es una aplicaci\u00f3n de escritorio que aplica el Teorema de Bayes para calcular probabilidades en un contexto industrial. Usando PySide6, la interfaz permite al usuario gestionar registros de f\u00e1bricas, introduciendo porcentajes de producci\u00f3n y defectos. La aplicaci\u00f3n recalcula autom\u00e1ticamente probabilidades condicionadas como P(ND|F), P(F|D) y P(F|ND), asegur\u00e1ndose de que los datos sean consistentes. Este enfoque interactivo muestra c\u00f3mo cambian las probabilidades al ajustar los par\u00e1metros.", None))
        self.tab_one.setTabText(self.tab_one.indexOf(self.tab_one_2), QCoreApplication.translate("MainWindow", u"Introducci\u00f3n", None))
        ___qtablewidgetitem = self.table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"F\u00e1brica", None));
        ___qtablewidgetitem1 = self.table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"P(F\u00e1brica)", None));
        ___qtablewidgetitem2 = self.table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"P(D|F\u00e1brica)", None));
        ___qtablewidgetitem3 = self.table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"P(ND|F\u00e1brica)", None));
        ___qtablewidgetitem4 = self.table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"P(F\u00e1brica|D)", None));
        ___qtablewidgetitem5 = self.table.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"P(F\u00e1brica|ND)", None));
        self.btn_add.setText(QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.btn_del.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
        self.tab_one.setTabText(self.tab_one.indexOf(self.tab_all), QCoreApplication.translate("MainWindow", u"F\u00e1bricas", None))
    # retranslateUi

