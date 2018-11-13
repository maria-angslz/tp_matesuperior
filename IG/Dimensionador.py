# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dimensionador.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dimensionador(object):
    def setupUi(self, Dimensionador):
        Dimensionador.setObjectName("Dimensionador")
        Dimensionador.resize(439, 176)
        Dimensionador.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(Dimensionador)
        self.centralwidget.setObjectName("centralwidget")
        self.Filas = QtWidgets.QLabel(self.centralwidget)
        self.Filas.setGeometry(QtCore.QRect(40, 70, 121, 20))
        self.Filas.setObjectName("Filas")
        self.buttonBox = QtWidgets.QDialogButtonBox(self.centralwidget)
        self.buttonBox.setGeometry(QtCore.QRect(140, 120, 161, 31))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.NumeroFilasA = QtWidgets.QSpinBox(self.centralwidget)
        self.NumeroFilasA.setGeometry(QtCore.QRect(190, 70, 161, 21))
        self.NumeroFilasA.setObjectName("NumeroFilasA")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 40, 16, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        Dimensionador.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Dimensionador)
        self.statusbar.setObjectName("statusbar")
        Dimensionador.setStatusBar(self.statusbar)

        self.retranslateUi(Dimensionador)
        self.buttonBox.rejected.connect(Dimensionador.close)
        QtCore.QMetaObject.connectSlotsByName(Dimensionador)

    def retranslateUi(self, Dimensionador):
        _translate = QtCore.QCoreApplication.translate
        Dimensionador.setWindowTitle(_translate("Dimensionador", "MainWindow"))
        self.Filas.setText(_translate("Dimensionador", "Dimension de la Matriz:"))
        self.label.setText(_translate("Dimensionador", "A"))

