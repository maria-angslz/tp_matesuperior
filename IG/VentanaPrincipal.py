# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VentanaPrincipal.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(563, 354)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../6634246081596847747.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(400, 280, 161, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 0, 131, 61))
        font = QtGui.QFont()
        font.setFamily("Footlight MT Light")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setScaledContents(False)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 251, 241))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMaximumSize(QtCore.QSize(800, 800))
        self.label_3.setObjectName("label_3")
        self.ingresoDatos = QtWidgets.QPushButton(self.centralwidget)
        self.ingresoDatos.setGeometry(QtCore.QRect(340, 40, 191, 31))
        self.ingresoDatos.setObjectName("ingresoDatos")
        self.SeleccionarMetodo = QtWidgets.QPushButton(self.centralwidget)
        self.SeleccionarMetodo.setGeometry(QtCore.QRect(340, 120, 191, 31))
        self.SeleccionarMetodo.setObjectName("SeleccionarMetodo")
        self.Salir = QtWidgets.QPushButton(self.centralwidget)
        self.Salir.setGeometry(QtCore.QRect(370, 200, 131, 23))
        self.Salir.setObjectName("Salir")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(280, 30, 41, 41))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(280, 110, 41, 41))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(310, 190, 41, 41))
        self.label_6.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 563, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionIngresar_Datos = QtWidgets.QAction(MainWindow)
        self.actionIngresar_Datos.setObjectName("actionIngresar_Datos")
        self.actionMetodo_de_resolucion = QtWidgets.QAction(MainWindow)
        self.actionMetodo_de_resolucion.setObjectName("actionMetodo_de_resolucion")
        self.actionFinalizar = QtWidgets.QAction(MainWindow)
        self.actionFinalizar.setObjectName("actionFinalizar")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TP MATEMATICA SUPERIOR"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-style:italic;\">Creado por Grupo Mixto_9 </span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#00aa00;\">SIEL</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/newPrefix/kubik.jpg\"/></p></body></html>"))
        self.ingresoDatos.setText(_translate("MainWindow", "Ingresar Datos"))
        self.SeleccionarMetodo.setText(_translate("MainWindow", "Seleccionar Metodo"))
        self.Salir.setText(_translate("MainWindow", "Salir"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/iconos/lapiz.jpg\"/></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/iconos/listado.jpg\"/></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/iconos/exit.jpg\"/></p></body></html>"))
        self.actionIngresar_Datos.setText(_translate("MainWindow", "Ingresar Datos"))
        self.actionMetodo_de_resolucion.setText(_translate("MainWindow", "Metodo de Resolución"))
        self.actionFinalizar.setText(_translate("MainWindow", "Finalizar"))

import imageLogo_rc
