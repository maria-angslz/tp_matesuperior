# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 18:26:29 2018

@author: sho_m
"""

import sys
from PyQt5 import uic, QtWidgets
from VentanaIngresoDatos import Ui_IngresoDatos
from Dimensionador import Ui_Dimensionador

qtCreatorFile = "VentanaPrincipal.ui" # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.ingresoDatos.clicked.connect(self.abrirIngresoDatos)
        
    def abrirIngresoDatos(self):       
        
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
        ventanaDimensionador = VentanaDimensionador(self)
        ventanaDimensionador._init_()
        
class VentanaDimensionador(QtWidgets.QMainWindow):        
        def _init_(self):
            self.ventana=QtWidgets.QMainWindow()
            self.ui=Ui_Dimensionador()
            self.ui.setupUi(self.ventana)
            self.ventana.show()  
     

if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
    
