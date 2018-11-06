# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VentanaNorma.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_VentanaNorma(object):
    def setupUi(self, VentanaNorma):
        VentanaNorma.setObjectName("VentanaNorma")
        VentanaNorma.resize(403, 246)
        VentanaNorma.setStyleSheet("background-color: rgb(245, 245, 245);")
        self.centralwidget = QtWidgets.QWidget(VentanaNorma)
        self.centralwidget.setObjectName("centralwidget")
        self.comboNormas = QtWidgets.QComboBox(self.centralwidget)
        self.comboNormas.setGeometry(QtCore.QRect(250, 20, 131, 21))
        self.comboNormas.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboNormas.setObjectName("comboNormas")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.botonCalcular = QtWidgets.QPushButton(self.centralwidget)
        self.botonCalcular.setGeometry(QtCore.QRect(160, 60, 91, 31))
        self.botonCalcular.setStyleSheet("background-color: rgb(239, 239, 239);")
        self.botonCalcular.setObjectName("botonCalcular")
        self.textoResultado = QtWidgets.QLabel(self.centralwidget)
        self.textoResultado.setGeometry(QtCore.QRect(20, 120, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.textoResultado.setFont(font)
        self.textoResultado.setObjectName("textoResultado")
        self.resultado = QtWidgets.QLabel(self.centralwidget)
        self.resultado.setGeometry(QtCore.QRect(200, 120, 81, 31))
        self.resultado.setText("")
        self.resultado.setObjectName("resultado")
        self.botonAceptar = QtWidgets.QPushButton(self.centralwidget)
        self.botonAceptar.setGeometry(QtCore.QRect(160, 170, 91, 31))
        self.botonAceptar.setObjectName("botonAceptar")
        VentanaNorma.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(VentanaNorma)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 403, 21))
        self.menubar.setObjectName("menubar")
        VentanaNorma.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(VentanaNorma)
        self.statusbar.setObjectName("statusbar")
        VentanaNorma.setStatusBar(self.statusbar)

        self.retranslateUi(VentanaNorma)
        QtCore.QMetaObject.connectSlotsByName(VentanaNorma)

    def retranslateUi(self, VentanaNorma):
        _translate = QtCore.QCoreApplication.translate
        VentanaNorma.setWindowTitle(_translate("VentanaNorma", "MainWindow"))
        self.label.setText(_translate("VentanaNorma", "Seleccione la norma a calcular:"))
        self.botonCalcular.setText(_translate("VentanaNorma", "Calcular"))
        self.textoResultado.setText(_translate("VentanaNorma", "El resultado obtenido es:"))
        self.botonAceptar.setText(_translate("VentanaNorma", "Aceptar"))

