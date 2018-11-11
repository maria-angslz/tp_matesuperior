# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VentanaMetodo.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_VentanaMetodo(object):
    def setupUi(self, VentanaMetodo):
        VentanaMetodo.setObjectName("VentanaMetodo")
        VentanaMetodo.resize(949, 556)
        self.centralwidget = QtWidgets.QWidget(VentanaMetodo)
        self.centralwidget.setObjectName("centralwidget")
        self.comboMetodos = QtWidgets.QComboBox(self.centralwidget)
        self.comboMetodos.setGeometry(QtCore.QRect(220, 20, 131, 21))
        self.comboMetodos.setObjectName("comboMetodos")
        self.comboMetodos.addItem("")
        self.comboMetodos.addItem("")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(160, 60, 71, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 180, 111, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 250, 71, 16))
        self.label_4.setObjectName("label_4")
        self.cotaError = QtWidgets.QTextEdit(self.centralwidget)
        self.cotaError.setGeometry(QtCore.QRect(150, 240, 121, 31))
        self.cotaError.setObjectName("cotaError")
        self.decimales = QtWidgets.QTextEdit(self.centralwidget)
        self.decimales.setGeometry(QtCore.QRect(150, 180, 121, 31))
        self.decimales.setObjectName("decimales")
        self.BotonCalcular = QtWidgets.QPushButton(self.centralwidget)
        self.BotonCalcular.setGeometry(QtCore.QRect(130, 330, 111, 31))
        self.BotonCalcular.setObjectName("BotonCalcular")
        self.BotonFinalizar = QtWidgets.QPushButton(self.centralwidget)
        self.BotonFinalizar.setGeometry(QtCore.QRect(590, 460, 101, 31))
        self.BotonFinalizar.setObjectName("BotonFinalizar")
        self.VectorInicial = QtWidgets.QTableView(self.centralwidget)
        self.VectorInicial.setGeometry(QtCore.QRect(20, 90, 331, 61))
        self.VectorInicial.setObjectName("VectorInicial")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(390, 10, 521, 251))
        self.tableView.setObjectName("tableView")
        self.tableView_2 = QtWidgets.QTableView(self.centralwidget)
        self.tableView_2.setGeometry(QtCore.QRect(390, 320, 521, 101))
        self.tableView_2.setObjectName("tableView_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(390, 280, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        VentanaMetodo.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(VentanaMetodo)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 949, 21))
        self.menubar.setObjectName("menubar")
        VentanaMetodo.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(VentanaMetodo)
        self.statusbar.setObjectName("statusbar")
        VentanaMetodo.setStatusBar(self.statusbar)

        self.retranslateUi(VentanaMetodo)
        QtCore.QMetaObject.connectSlotsByName(VentanaMetodo)

    def retranslateUi(self, VentanaMetodo):
        _translate = QtCore.QCoreApplication.translate
        VentanaMetodo.setWindowTitle(_translate("VentanaMetodo", "MainWindow"))
        self.comboMetodos.setItemText(0, _translate("VentanaMetodo", "Jacobi"))
        self.comboMetodos.setItemText(1, _translate("VentanaMetodo", "Gauss Seidel"))
        self.label.setText(_translate("VentanaMetodo", "Seleccione un metodo iterativo:"))
        self.label_2.setText(_translate("VentanaMetodo", "Vector Inicial"))
        self.label_3.setText(_translate("VentanaMetodo", "Cantidad de decimales"))
        self.label_4.setText(_translate("VentanaMetodo", "Cota de error"))
        self.BotonCalcular.setText(_translate("VentanaMetodo", "Calcular"))
        self.BotonFinalizar.setText(_translate("VentanaMetodo", "Finalizar"))
        self.label_5.setText(_translate("VentanaMetodo", "Resultados: "))

