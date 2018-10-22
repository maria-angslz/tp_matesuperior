# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VentanaIngresoDatos.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_IngresoDatos(object):
    def setupUi(self, IngresoDatos):
        IngresoDatos.setObjectName("IngresoDatos")
        IngresoDatos.resize(762, 441)
        IngresoDatos.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(IngresoDatos)
        self.centralwidget.setObjectName("centralwidget")
        self.Coeficientes = QtWidgets.QTableView(self.centralwidget)
        self.Coeficientes.setGeometry(QtCore.QRect(10, 40, 231, 281))
        self.Coeficientes.setObjectName("Coeficientes")
        self.Incognitas = QtWidgets.QTableView(self.centralwidget)
        self.Incognitas.setGeometry(QtCore.QRect(290, 40, 121, 281))
        self.Incognitas.setObjectName("Incognitas")
        self.TerminosIndependientes = QtWidgets.QTableView(self.centralwidget)
        self.TerminosIndependientes.setGeometry(QtCore.QRect(470, 40, 121, 281))
        self.TerminosIndependientes.setObjectName("TerminosIndependientes")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(420, 170, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(250, 140, 31, 51))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_2.setObjectName("label_2")
        self.BotonDimensionar = QtWidgets.QPushButton(self.centralwidget)
        self.BotonDimensionar.setGeometry(QtCore.QRect(150, 350, 131, 31))
        self.BotonDimensionar.setObjectName("BotonDimensionar")
        self.validarMatrices = QtWidgets.QPushButton(self.centralwidget)
        self.validarMatrices.setGeometry(QtCore.QRect(610, 170, 141, 41))
        self.validarMatrices.setObjectName("validarMatrices")
        self.BotonNorma = QtWidgets.QPushButton(self.centralwidget)
        self.BotonNorma.setGeometry(QtCore.QRect(330, 350, 131, 31))
        self.BotonNorma.setObjectName("BotonNorma")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(110, 0, 21, 31))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(510, 0, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(330, 0, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.botonGuardar = QtWidgets.QPushButton(self.centralwidget)
        self.botonGuardar.setGeometry(QtCore.QRect(640, 340, 101, 41))
        self.botonGuardar.setStyleSheet("background-color: rgb(144, 229, 91);\n"
"selection-background-color: rgb(0, 85, 0);\n"
"\n"
"")
        self.botonGuardar.setObjectName("botonGuardar")
        IngresoDatos.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(IngresoDatos)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 762, 21))
        self.menubar.setObjectName("menubar")
        IngresoDatos.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(IngresoDatos)
        self.statusbar.setObjectName("statusbar")
        IngresoDatos.setStatusBar(self.statusbar)

        self.retranslateUi(IngresoDatos)
        QtCore.QMetaObject.connectSlotsByName(IngresoDatos)

    def retranslateUi(self, IngresoDatos):
        _translate = QtCore.QCoreApplication.translate
        IngresoDatos.setWindowTitle(_translate("IngresoDatos", "MainWindow"))
        self.label.setText(_translate("IngresoDatos", "="))
        self.label_2.setText(_translate("IngresoDatos", "."))
        self.BotonDimensionar.setText(_translate("IngresoDatos", "Dimensionar Matrices"))
        self.validarMatrices.setText(_translate("IngresoDatos", "Validar Matrices"))
        self.BotonNorma.setText(_translate("IngresoDatos", "Obtener normas"))
        self.label_3.setText(_translate("IngresoDatos", "A"))
        self.label_4.setText(_translate("IngresoDatos", "B"))
        self.label_5.setText(_translate("IngresoDatos", "X"))
        self.botonGuardar.setText(_translate("IngresoDatos", "Guardar"))

