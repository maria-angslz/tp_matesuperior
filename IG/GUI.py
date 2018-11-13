# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 18:26:29 2018

@author: sho_m
"""

import sys
from PyQt5 import uic, QtWidgets, QtGui
from PyQt5.QtWidgets import QMessageBox, QTableWidget,QTableWidgetItem
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

def qt2list(modelo):
    matriz = []
    x_loop_must_break = False;
    rowCount = modelo.rowCount()
    columnCount = modelo.columnCount()
    for i in range(0,rowCount):
        for j in range(0,columnCount):
            matriz.append(modelo.item(i,j).text())
    return matriz

class MyApp(QtWidgets.QMainWindow,Ui_MainWindow):
    pepe = QtGui.QStandardItemModel()
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
    pepe = QtGui.QStandardItemModel()
    pepe2 = QtGui.QStandardItemModel()
    yaAdvertido = False;
    def _init_(self):
        self.ventana=QtWidgets.QMainWindow()
        self.ui=Ui_VentanaMetodo()
        self.ui.setupUi(self.ventana)
        self.ventana.show()
        self.vectorInicial()
        self.ui.BotonCalcular.clicked.connect(self.calcularMetodo)
        self.ui.BotonFinalizar.clicked.connect(self.ventana.hide)

    def vectorInicial(self):
        self.ui.VectorInicial.setModel(self.vectorIni)
        self.vectorIni.clear()
        self.vectorIni.setRowCount(1);
        self.vectorIni.setColumnCount(Functions.columnasA);    

    def calcularMetodo(self):
        header = ['Paso']
        header = header + Functions.matrizX
        header.append('Norma')

        self.ui.tableView_2.setModel(self.pepe2)

        self.validarVectorInicial(self.vectorIni)
        self.validarCampos(self.ui.decimales, "int")
        self.validarCampos(self.ui.cotaError, "float")
        eleccionMetodo = self.ui.comboMetodos.currentIndex()

        #print(eleccionMetodo)
        if not(self.yaAdvertido):
            if eleccionMetodo == 0:
                matrizSolucion = Functions.doJacobi(Functions.matrizA, Functions.matrizB, pasarMatriz(self.vectorIni), float(self.ui.cotaError.toPlainText()), int(self.ui.decimales.toPlainText()))
            elif eleccionMetodo == 1:
                matrizSolucion = Functions.doGaussSeidel(Functions.matrizA, Functions.matrizB, pasarMatriz(self.vectorIni), float(self.ui.cotaError.toPlainText()), int(self.ui.decimales.toPlainText()))
                  
        self.yaAdvertido = False
        self.ui.tableView.setModel(self.pepe)
        self.pepe.clear()
        rowCount = np.size(matrizSolucion,0)
        columnCount = len(header)
        self.pepe.setRowCount(rowCount);
        self.pepe.setColumnCount(columnCount);
        self.pepe.setHorizontalHeaderLabels(header)
        #TODO aca va a completar el jacobi a la tabla hay que hacerlo funcion y repetirlo con el otro metodo
        for i in range(0,rowCount):
            for j in range(0,columnCount):
                self.pepe.setItem(i, j, QtGui.QStandardItem(str(matrizSolucion[i][j])))
        self.pepe2.clear()
        self.pepe2.setRowCount(1);
        self.pepe2.setColumnCount(len(Functions.matrizX));
        self.pepe2.setHorizontalHeaderLabels(Functions.matrizX)
        self.pepe2.setVerticalHeaderLabels(["Resultado"])
        j = 0
        for j in range(1,columnCount-1):
            #print(str(matrizSolucion[rowCount-1][j]))
            self.pepe2.setItem(0, j-1, QtGui.QStandardItem(str(matrizSolucion[rowCount-1][j])))


    def validarCampos(self, qtextEdit, tipo):
        if qtextEdit.toPlainText() is '':
            if self.yaAdvertido is False:
                QMessageBox.information(self,"Advertencia","Complete el/los campos")
                self.yaAdvertido = True;
        
        elif tipo == "int":
            if not(Functions.is_digit_int(qtextEdit.toPlainText())):
                if self.yaAdvertido is False:
                    QMessageBox.information(self,"Advertencia","Complete el/los campos correctamente")
                    self.yaAdvertido = True;
                
        else:
            if not(Functions.is_digit(qtextEdit.toPlainText())):
                if self.yaAdvertido is False:
                    QMessageBox.information(self,"Advertencia","Complete el/los campos correctamente")
                    self.yaAdvertido = True;
            
            
    def validarVectorInicial(self,modelo):
        
        columnCount = modelo.columnCount()
        for j in range(0,columnCount):
            if modelo.item(0,j) is None:              
                break;
            elif modelo.item(0,j).text() == '':                                 
                break;
            else:
                if (not(Functions.is_digit(modelo.item(0,j).text()))):                   
                    break;
                
        if modelo.item(0,j) is None:           
            if self.yaAdvertido is False:
                QMessageBox.information(self,"Advertencia","Complete el vector inicial")
                self.yaAdvertido = True;
        elif modelo.item(0,j).text() == '':    
            if self.yaAdvertido is False:
                QMessageBox.information(self,"Advertencia","Complete el vector inicial")
                self.yaAdvertido = True;
        else:
            if (not(Functions.is_digit(modelo.item(0,j).text()))):
                if self.yaAdvertido is False:
                    QMessageBox.information(self,"Advertencia","Complete correctamente el vector")
                    self.yaAdvertido = True;
         

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
        self.ui.BotonNorma.setEnabled(False)
        self.ventana.show()
        self.ui.botonGuardar.clicked.connect(self.guardarMatriz)
        self.ui.BotonDimensionar.clicked.connect(self.abrirDimensionador)
        self.ui.validarMatrices.clicked.connect(self.validarMatriz)
        self.ui.BotonNorma.clicked.connect(self.abrirNorma)
     
    def guardarMatriz(self):
        Functions.matrizA = pasarMatriz(self.modelA)
        Functions.matrizB = pasarMatriz(self.modelB)
        Functions.matrizX = qt2list(self.modelX)
        self.ventana.hide()

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
                    if (validador == "digito" and not(Functions.is_digit(modelo.item(i,j).text()))) or (validador == "letra" and Functions.is_digit(modelo.item(i,j).text())):
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
            if (validador == "digito" and not(Functions.is_digit(modelo.item(i,j).text()))) or (validador == "letra" and Functions.is_digit(modelo.item(i,j).text())):
                if self.yaAdvertido is False:
                    QMessageBox.information(self,"Advertencia","Complete correctamente las matrices")
                    self.yaAdvertido = True;
                    
    
                                   
    def validaDiagonalmenteDominante(self, pepe): #recibo la matriz                 
       #aqui se valida si es diagonalmente dominante, usando la funcion de functions.py
       if Functions.diagonalDomMatrix(pepe): #le paso la matriz
            QMessageBox.information(self,"Valido","Matriz correcta") 
            self.ui.botonGuardar.setEnabled(True)
            self.ui.BotonNorma.setEnabled(True)
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
        self.modelA.setRowCount(filas);
        self.modelA.setColumnCount(filas);
        Functions.columnasA = filas;

        
    def matrizX(self):
        self.ui.Incognitas.setModel(self.modelX)
        self.modelX.clear()
        filas = ventanaDimensionador.getFilasA()      
        self.modelX.setRowCount(filas);
        self.modelX.setColumnCount(1);
                
    def matrizB(self):
        self.ui.TerminosIndependientes.setModel(self.modelB)
        self.modelB.clear()
        filas = ventanaDimensionador.getFilasA()
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
        #print()
        #print(numNorma)
        #print()
        #print(resultadoNorma)

        self.ui.textoResultado.show()
        self.ui.resultado.setNum(resultadoNorma)
        self.ui.resultado.show()
        

if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
    
