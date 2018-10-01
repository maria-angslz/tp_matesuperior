# -*- coding: UTF-8 -*-

#######################################################
## Funciones del tp de mate superior 2018 2cuatri    ##
## Date: 01/10/2018                                  ##
##   Grupo Mixto 9                                   ##
#######################################################
import numpy as np

def createMatrix(Rows, Cols):
	"""
	funcion piola para armar una matriz con valores secuenciales
	Parameters
	----------
	Rows: int
		Cantidad de filas
	Cols: int
		Cantidad de columnas
	""" 
	x = range(Rows*Cols)
	x = np.reshape(x,(Rows, Cols))
	"""
	#descomentar para generar una diagonalmente dominante
	x = np.array([[ 40., 7.,   5.],
		[ 5., 90.,  7.],
		[20., 7., 50.]])
	"""
	return x
#estrictamente dominante diagonalmente cuando los elementos de la 
#diagonal principal son mayores en valor absoluto, 
#que la suma de los valores absolutos de los demás elementos de la fila correspondiente

def diagonalDomMatrix(aMatrix):
    """
    funcion que verifica si una matriz es sdominante diagonalmene

    Parameters
    ----------
    Matrix
    	aMatrix: matriz a verificar du diagonalidad

    Returns
    -------
    Bool
    	1: es diagonalmente dominante
    	0: no es diagonalmete dominante
    """
    Coef = np.diag(np.abs(aMatrix)) # Busco los coeficientes
    Sum = np.sum(np.abs(aMatrix), axis=1) - Coef # busco una suma de fila sin diagonal
    if np.all(Coef > Sum):
        return 1
    else:
        return 0
    return
