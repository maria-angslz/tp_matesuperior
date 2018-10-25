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

def normaXMatrix (numNorma, aMatrix):
    """
    calcula la norma X de una matriz
    norma 1 : maxmo de la sma de columnas
    norma 2 : la norma euclidiana
    norma 3:  maximo absoluto de la suma de filas

    Parameters
    ----------
    aMatrix: matriz la cual se calcula su norma

    numNorma: el tipo de norma a calcular


    Returns
    -------
    float
        el valor de la norma
    """
    if numNorma == 1:
        norm = np.linalg.norm(aMatrix)
    elif (numNorma == 2 or  numNorma == 3): #el maximo absoludo de la suma de las filas
        for rowNum in range(0, len(aMatrix)-1):
            Sum = np.sum(aMatrix, axis = numNorma - 2)
            norm = max(Sum)

    else:
         raise Exception("valor de la norma no soportado")

    return norm

def getInvDiagonal (aMatrix, decimales):
    """
    retorna la inversa de la matriz diagonal de una matriz dada
    
    Parameters
    ----------
    aMatrix: matriz dada para sacar la inversa de su diagonal
    decimales: decimales para redondeo
    """
    
    matrizDiagonal = np.diagflat(np.diag(aMatrix))
    return np.around(np.linalg.inv(matrizDiagonal), decimals = decimales)


def getTMatrix (aMatrix, decimales):
    """
    saca una matriz T necesaria para el calculo de Jacobi 
    
    Parameters
    ----------
    aMatrix: matriz usada para el calculo de T
    decimales: decimales para redondeo
    """
    matrizTriInf = np.negative(np.tril(aMatrix,-1)) #matriz triangular inferior en negativo
    matrizTriSup = np.negative(np.triu(aMatrix,1)) #matriz triangular superior en negativo
    matrizSumaDiagInfSup = np.add(matrizTriInf,matrizTriSup)
    matrizInvDiagonal = getInvDiagonal(aMatrix,decimales)
    return np.around(np.matmul(matrizInvDiagonal,matrizSumaDiagInfSup), decimals = decimales)
    
def getCMatrix (aMatrixCoeficients, aMatrixIndepTerms, decimales):
    """
    saca una matriz C necesaria para el calculo de Jacobi
    
    Parameters
    ----------
    aMatrixCoeficients: matriz de coeficientes 
    aMatrixIndepTerms: matriz de terminos independientes
    decimales = decimales para redondeo
    """
    matrizInvDiagonal = getInvDiagonal(aMatrixCoeficients,decimales)
    return np.around(np.matmul(matrizInvDiagonal,aMatrixIndepTerms), decimals = decimales)

def getVecIPlus (tMatrix,cMatrix,vectorI):
    """
    saca un vector i+1 dado un vector i
    
    Parameters
    ----------
    vectorI: vector i
    tMatrix: matriz T
    cMatrix: matriz C
    """
    
    return np.add(np.transpose(np.matmul(tMatrix,np.transpose(vectorI))),np.transpose(cMatrix))
        
def doJacobi (aMatrixCoeficients, aMatrixIndepTerms, inicialVec, error, decimales):
    """
    funcion que realiza el metodo de Jacobi
    
    Parameters
    ----------
    aMatrixCoeficients: matriz de coeficientes
    aMatrixIndepTerms: matriz de terminos independientes
    inicialVec: vector inicial
    decimales: decimales para redondeo
    """
    
    tMatrix = getTMatrix(aMatrixCoeficients,decimales)
    cMatrix = getCMatrix(aMatrixCoeficients,aMatrixIndepTerms,decimales)
    
    vectorI = np.around(getVecIPlus(tMatrix, cMatrix, inicialVec),decimals = decimales)
    
    restaAbsoluto = np.absolute(np.subtract(vectorI,inicialVec))
    
    while (np.around(normaXMatrix(1,restaAbsoluto),decimals = decimales) > error):
        vectorIPlus = np.around(getVecIPlus(tMatrix, cMatrix, vectorI),decimals = decimales)
        restaAbsoluto = np.absolute(np.subtract(vectorI,vectorIPlus))
        vectorI = vectorIPlus
        
    return vectorIPlus