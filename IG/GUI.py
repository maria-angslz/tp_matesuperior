# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 18:26:29 2018

@author: sho_m
"""

import sys
from PyQt5 import uic, QtWidgets, QtGui
from PyQt5.QtWidgets import QMessageBox
from VentanaIngresoDatos import Ui_IngresoDatos
from Dimensionador import Ui_Dimensionador
import Functions

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
    yaAdvertido = False;
    modelA = QtGui.QStandardItemModel()
    modelX = QtGui.QStandardItemModel()
    modelB = QtGui.QStandardItemModel()
    
    def _init_(self):
        self.ventana=QtWidgets.QMainWindow()
        self.ui=Ui_IngresoDatos()
        self.ui.setupUi(self.ventana)
        self.ventana.show()        
        self.ui.BotonDimensionar.clicked.connect(self.abrirDimensionador)
        self.ui.validarMatrices.clicked.connect(self.validarMatriz)
        #self.ui.BotonNorma.clicked.connect(self.abrirNorma)
        
    def abrirDimensionador(self):
        global ventanaDimensionador
        ventanaDimensionador = VentanaDimensionador(self)
        ventanaDimensionador._init_()
        
    def validarMatriz(self):
        self.validaMatrizCompleta(self.modelA)
        self.validaMatrizCompleta(self.modelX)
        self.validaMatrizCompleta(self.modelB)
        self.yaAdvertido = False;
        #habria que crear la matriz A seteandole los valores que estan cargados en el modelo usando numpy      
        self.validaDiagonalmenteDominante()  #le paso la matriz generada en la linea anterior  

    def validaMatrizCompleta(self, modelo):
        x_loop_must_break = False;
        rowCount = modelo.rowCount()
        columnCount = modelo.columnCount()
        for i in range(0,rowCount):
            for j in range(0,columnCount):
                if modelo.item(i,j) is None:
                    x_loop_must_break = True
                    break;
                else:
                    if modelo.item(i,j).text() == '':                       
                        x_loop_must_break = True
                        break;
            if x_loop_must_break: break;
        
        if modelo.item(i,j) is None:           
            if self.yaAdvertido is False:
                QMessageBox.information(self,"Advertencia","Complete las matrices")
                self.yaAdvertido = True;
        else:    
            if modelo.item(i,j).text() == '':                
                if self.yaAdvertido is False:
                    QMessageBox.information(self,"Advertencia","Complete las matrices")
                    self.yaAdvertido = True;
                                   

    def validaDiagonalmenteDominante(self): #recibo la matriz                 
       #aqui se valida si es diagonalmente dominante, usando la funcion de functions.py
       """if Functions.diagonalDomMatrix(): #le paso la matriz
            QMessageBox.information(self,"Valido","Matriz correcta")            
       else:
            QMessageBox.information(self,"No valido","Debe insertar una matriz diagonalmente dominante")"""
        
        
    def introduceMatrices(self):
        self.matrizA()
        self.matrizX()
        self.matrizB()      
        ventanaDimensionador.escondete()
        self.ventana.show()
    
    def matrizA(self):
        self.ui.Coeficientes.setModel(self.modelA)
        self.modelA.clear()
        filas = ventanaDimensionador.getFilasA()
        columnas = ventanaDimensionador.getColumnasA()
        self.modelA.setRowCount(filas);
        self.modelA.setColumnCount(columnas);
        
        
    def matrizX(self):
        self.ui.Incognitas.setModel(self.modelX)
        self.modelX.clear()
        filas = ventanaDimensionador.getFilasX()      
        self.modelX.setRowCount(filas);
        self.modelX.setColumnCount(1);
                
    def matrizB(self):
        self.ui.TerminosIndependientes.setModel(self.modelB)
        self.modelB.clear()
        filas = ventanaDimensionador.getFilasB()
        self.modelB.setRowCount(filas);
        self.modelB.setColumnCount(1);


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
    
