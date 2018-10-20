# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 18:26:29 2018

@author: sho_m
"""

import sys
from PyQt5 import uic, QtWidgets, QtGui 
from VentanaIngresoDatos import Ui_IngresoDatos
from Dimensionador import Ui_Dimensionador

qtCreatorFile = "VentanaPrincipal.ui" # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
ventanaIngreso = 0
ventanaDimensionador = 0

class MyApp(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.ingresoDatos.clicked.connect(self.abrirIngresoDatos)
        self.Salir.clicked.connect(self.close)
        
    def abrirIngresoDatos(self):       
        global ventanaIngreso
        ventanaIngreso = VentanaIngresoDatos(self)
        ventanaIngreso._init_()
        
        
class VentanaIngresoDatos(QtWidgets.QMainWindow):
    def _init_(self):
        self.ventana=QtWidgets.QMainWindow()
        self.ui=Ui_IngresoDatos()
        self.ui.setupUi(self.ventana)
        self.ventana.show()        
        self.ui.BotonDimensionar.clicked.connect(self.abrirDimensionador)
    
    def abrirDimensionador(self):
        global ventanaDimensionador
        ventanaDimensionador = VentanaDimensionador(self)
        ventanaDimensionador._init_()
        
        
    def introduceMatrices(self):
        self.matrizA()
        self.matrizX()
        self.matrizB()      
        ventanaDimensionador.escondete()
        self.ventana.show()
    
    def matrizA(self):
        modelA = QtGui.QStandardItemModel()
        self.ui.Coeficientes.setModel(modelA)
        filas = ventanaDimensionador.getFilasA()
        columnas = ventanaDimensionador.getColumnasA()
        modelA.setRowCount(filas);
        modelA.setColumnCount(columnas);
        
    def matrizX(self):
        modelX = QtGui.QStandardItemModel()
        self.ui.Incognitas.setModel(modelX)
        filas = ventanaDimensionador.getFilasX()      
        modelX.setRowCount(filas);
        modelX.setColumnCount(1);
                
    def matrizB(self):
        modelB = QtGui.QStandardItemModel()
        self.ui.TerminosIndependientes.setModel(modelB)
        filas = ventanaDimensionador.getFilasB()
        modelB.setRowCount(filas);
        modelB.setColumnCount(1);


class VentanaDimensionador(QtWidgets.QMainWindow):        
        def _init_(self):
            self.ventana=QtWidgets.QMainWindow()
            self.ui=Ui_Dimensionador()
            self.ui.setupUi(self.ventana)
            self.ventana.show()            
            self.ui.buttonBox.accepted.connect(ventanaIngreso.introduceMatrices)            
            
        def getFilasA(self):
            return self.ui.NumeroFilasA.value()
        
        def getColumnasA(self):
            return self.ui.NumeroColumnasA.value()
        
        def getFilasX(self):
            return self.ui.NumeroFilasX.value()
        
        def getFilasB(self):
            return self.ui.NumeroFilasB.value()
            
        def escondete(self):
            self.ventana.close()

if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
    
