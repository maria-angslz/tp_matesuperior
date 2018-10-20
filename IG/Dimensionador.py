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
        Dimensionador.resize(557, 199)
        Dimensionador.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(Dimensionador)
        self.centralwidget.setObjectName("centralwidget")
        self.Filas = QtWidgets.QLabel(self.centralwidget)
        self.Filas.setGeometry(QtCore.QRect(40, 70, 81, 16))
        self.Filas.setObjectName("Filas")
        self.Columnas = QtWidgets.QLabel(self.centralwidget)
        self.Columnas.setGeometry(QtCore.QRect(30, 100, 101, 16))
        self.Columnas.setObjectName("Columnas")
        self.buttonBox = QtWidgets.QDialogButtonBox(self.centralwidget)
        self.buttonBox.setGeometry(QtCore.QRect(190, 140, 161, 31))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(150, 30, 381, 91))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.NumeroFilasB = QtWidgets.QSpinBox(self.layoutWidget)
        self.NumeroFilasB.setObjectName("NumeroFilasB")
        self.gridLayout.addWidget(self.NumeroFilasB, 1, 2, 1, 1)
        self.NumeroColumnasA = QtWidgets.QSpinBox(self.layoutWidget)
        self.NumeroColumnasA.setObjectName("NumeroColumnasA")
        self.gridLayout.addWidget(self.NumeroColumnasA, 2, 0, 1, 1)
        self.NumeroFilasX = QtWidgets.QSpinBox(self.layoutWidget)
        self.NumeroFilasX.setObjectName("NumeroFilasX")
        self.gridLayout.addWidget(self.NumeroFilasX, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)
        self.NumeroFilasA = QtWidgets.QSpinBox(self.layoutWidget)
        self.NumeroFilasA.setObjectName("NumeroFilasA")
        self.gridLayout.addWidget(self.NumeroFilasA, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
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
        self.Filas.setText(_translate("Dimensionador", "Numero de filas"))
        self.Columnas.setText(_translate("Dimensionador", "Numero de columnas"))
        self.label_2.setText(_translate("Dimensionador", "X"))
        self.label_3.setText(_translate("Dimensionador", "B"))
        self.label.setText(_translate("Dimensionador", "A"))

