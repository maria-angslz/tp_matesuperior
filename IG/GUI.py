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
from VentanaNorma import Ui_VentanaNorma
from VentanaMetodo import Ui_VentanaMetodo
import Functions
import numpy as np

qtCreatorFile = "VentanaPrincipal.ui" # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
ventanaIngreso = 0
ventanaDimensionador = 0
ventanaNorma = 0
ventanaMetodo = 0

#matrizAcalcular; 


def pasarMatriz(modelo):        
    matriz = tabla2matix(modelo)
    return matriz

def tabla2matix(modelo):
    x_loop_must_break = False;
    rowCount = modelo.rowCount()
    columnCount = modelo.columnCount()
    matriz = Functions.createMatrix(rowCount,columnCount)
    for i in range(0,rowCount):
        for j in range(0,columnCount):
            matriz[i, j] = float(modelo.item(i,j).text())
    return matriz

def tabla2matix2(modelo):
    print()
    #matriz = range(0) 
    #x_loop_must_break = False;
    #rowCount = modelo.rowCount()
    #columnCount = modelo.columnCount()
    #matriz[rowCount][columnCount] = 0
    #for i in range(0,rowCount):
        #for j in range(0,columnCount):
            #matriz[i, j] = (modelo.item(i,j).text())
    #return matriz    

class MyApp(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.ingresoDatos.clicked.connect(self.abrirIngresoDatos)
        self.Salir.clicked.connect(self.close)
        self.SeleccionarMetodo.clicked.connect(self.abrirMetodo)

    def abrirIngresoDatos(self):
        global ventanaIngreso
        ventanaIngreso = VentanaIngresoDatos(self)
        ventanaIngreso._init_()

    def abrirMetodo(self):
        global ventanaMetodo
        ventanaMetodo = VentanaMetodo(self)
        ventanaMetodo._init_()


class VentanaMetodo(QtWidgets.QMainWindow):
    vectorIni = QtGui.QStandardItemModel()
    def _init_(self):
        self.ventana=QtWidgets.QMainWindow()
        self.ui=Ui_VentanaMetodo()
        self.ui.setupUi(self.ventana)
        self.ventana.show()
        self.vectorInicial()
        self.ui.BotonCalcular.clicked.connect(self.calcularMetodo)

    def vectorInicial(self):
        self.ui.VectorInicial.setModel(self.vectorIni)
        self.vectorIni.clear()
        self.vectorIni.setRowCount(1);
        self.vectorIni.setColumnCount(Functions.columnasA);    

    def calcularMetodo(self):
        solJacobi = Functions.doJacobi(Functions.matrizA, Functions.matrizB, pasarMatriz(self.vectorIni), float(self.ui.cotaError.toPlainText()), int(self.ui.decimales.toPlainText()))

        

class VentanaIngresoDatos(QtWidgets.QMainWindow):
    yaAdvertido = False;
    modelA = QtGui.QStandardItemModel()
    modelX = QtGui.QStandardItemModel()
    modelB = QtGui.QStandardItemModel()
    
    def _init_(self):
        self.ventana=QtWidgets.QMainWindow()
        self.ui=Ui_IngresoDatos()
        self.ui.setupUi(self.ventana)
        self.ui.botonGuardar.setEnabled(False)
        self.ventana.show()
        self.ui.botonGuardar.clicked.connect(self.guardarMatriz)
        self.ui.BotonDimensionar.clicked.connect(self.abrirDimensionador)
        self.ui.validarMatrices.clicked.connect(self.validarMatriz)
        self.ui.BotonNorma.clicked.connect(self.abrirNorma)
     
    def guardarMatriz(self):
        Functions.matrizA = pasarMatriz(self.modelA)
        Functions.matrizB = pasarMatriz(self.modelB)
        row = [self.modelX.item(0,0).text()]
        print(row)
        row = [self.modelX.item(1,0).text()]
        print(row)





    def abrirNorma(self):
        global ventanaNorma
        ventanaNorma = VentanaNorma(self)
        ventanaNorma._init_()
        
    def abrirDimensionador(self):
        global ventanaDimensionador
        ventanaDimensionador = VentanaDimensionador(self)
        ventanaDimensionador._init_()
        
    def validarMatriz(self):
        self.validaMatrizCompleta(self.modelA, "digito")
        self.validaMatrizCompleta(self.modelX, "letra")
        self.validaMatrizCompleta(self.modelB, "digito")
        if not(self.yaAdvertido):
            Functions.matrizA = pasarMatriz(self.modelA)
            self.validaDiagonalmenteDominante(Functions.matrizA) 
        self.yaAdvertido = False;
    
        
    def validaMatrizCompleta(self, modelo, validador):
        x_loop_must_break = False;
        rowCount = modelo.rowCount()
        columnCount = modelo.columnCount()
        for i in range(0,rowCount):
            for j in range(0,columnCount):
                if modelo.item(i,j) is None:
                    x_loop_must_break = True
                    break;
                elif modelo.item(i,j).text() == '':                  
                    x_loop_must_break = True
                    break;
                else:
                    if (validador == "digito" and not(modelo.item(i,j).text().isdigit())) or (validador == "letra" and modelo.item(i,j).text().isdigit()):
                        x_loop_must_break = True
                        break;
            if x_loop_must_break: break;
        
        if modelo.item(i,j) is None:           
            if self.yaAdvertido is False:
                QMessageBox.information(self,"Advertencia","Complete las matrices")
                self.yaAdvertido = True;
        elif modelo.item(i,j).text() == '':    
            if self.yaAdvertido is False:
                QMessageBox.information(self,"Advertencia","Complete las matrices")
                self.yaAdvertido = True;
        else:
            if (validador == "digito" and not(modelo.item(i,j).text().isdigit())) or (validador == "letra" and modelo.item(i,j).text().isdigit()):
                if self.yaAdvertido is False:
                    QMessageBox.information(self,"Advertencia","Complete correctamente las matrices")
                    self.yaAdvertido = True;
                                       
    def validaDiagonalmenteDominante(self, pepe): #recibo la matriz                 
       #aqui se valida si es diagonalmente dominante, usando la funcion de functions.py
       if Functions.diagonalDomMatrix(pepe): #le paso la matriz
            QMessageBox.information(self,"Valido","Matriz correcta") 
            self.ui.botonGuardar.setEnabled(True)
       else:
            QMessageBox.information(self,"No valido","Debe insertar una matriz diagonalmente dominante")
        
        
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
            self.ui.NumeroColumnasA.setEnabled(False)
            self.ventana.show()            
            self.ui.buttonBox.accepted.connect(ventanaIngreso.introduceMatrices)            
            
        def getFilasA(self):
            return self.ui.NumeroFilasA.value()
        
        def getColumnasA(self):
            self.ui.NumeroColumnasA.setValue(self.getFilasA())
            Functions.columnasA = self.ui.NumeroColumnasA.value()
            return self.ui.NumeroColumnasA.value()
        
        def getFilasX(self):
            return self.ui.NumeroFilasX.value()
        
        def getFilasB(self):
            return self.ui.NumeroFilasB.value()
            
        def escondete(self):
            self.ventana.close()
            
            
class VentanaNorma(QtWidgets.QMainWindow):
    def _init_(self):
        self.ventana=QtWidgets.QMainWindow()
        self.ui=Ui_VentanaNorma()
        self.ui.setupUi(self.ventana)
        self.ui.textoResultado.hide()
        self.ui.resultado.hide()
        self.ui.comboNormas.addItem("Norma 1");
        self.ui.comboNormas.addItem("Norma 2");
        self.ui.comboNormas.addItem("Norma Infinito");
        self.ventana.show()
        self.ui.botonCalcular.clicked.connect(self.calculaNorma)
        self.ui.botonAceptar.clicked.connect(self.ventana.close)     
       
    def calculaNorma(self):
        numNorma = self.ui.comboNormas.currentIndex() + 1
        resultadoNorma = Functions.normaXMatrix(numNorma,  Functions.matrizA)  #se le debe pasar la matriz generada con los valores de la ventanaIngresaDatos
        #resultadoNorma = 0
        print()
        print(numNorma)
        print()
        print(resultadoNorma)

        self.ui.textoResultado.show()
        self.ui.resultado.setNum(resultadoNorma)
        self.ui.resultado.show()
        

if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
    
