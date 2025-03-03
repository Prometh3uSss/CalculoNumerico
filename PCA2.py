# -*- coding: utf-8 -*-
"""
Created on Mon May 25 18:30:30 2020

@author: Luis Miguel Sotamba 
"""

"""
No leer imágenes muy grandes. Aún falta optimizar 
el cálculo de los autovalores y autovectores.
"""

import matplotlib.image as mpimg 
import matplotlib.pyplot as plt
import numpy as np
from sklearn.decomposition import PCA
import warnings 

warnings.filterwarnings("ignore")

#verificación del error
def error(e,lambda_k, lambda_k_m1,k):
    
    if(k<=1):
        return False
    else:
        if(np.abs((lambda_k-lambda_k_m1)/lambda_k)<e):
            return True
        return False
    
#Hotelling Deflation
def deflation(A,eigenValue,eigenVector):
    return np.subtract(A,(eigenValue*eigenVector.dot(eigenVector.T))) 
    
def metodoPotencia(e,x0,A):
    y_k=x0/np.linalg.norm(x0)#Encuentro mi y) inicial dividiendo mi vector inicial para su norma
    lambda_k=1#Inicializacion de lambda k
    lambda_k_m1=0#Inicializacion de lambda k-1
    k=0#Inicialización de la variable que mantiene rastro de las iteraciones
    while(error(e,lambda_k,lambda_k_m1,k)==False):
        y_k_m1=y_k
        x_k=A.dot(y_k_m1)
        y_k=x_k/np.linalg.norm(x_k)
        lambda_k_m1=lambda_k
        lambda_k=((y_k).T).dot(A).dot(y_k)
        k=k+1
    
    return lambda_k,k,y_k,deflation(A,lambda_k,y_k)

#cantidad de información que aporta cada componente.
#Con los autovalores, divido cada autovalor para la suma de todos ellos.
#Así obtengo la información que aportan
def varianzaAportada(lambdas):
    porcentaje=np.zeros(lambdas.shape)
    suma=np.sum(lambdas)
    for i in range(lambdas.shape[0]):
        porcentaje[i]=lambdas[i]/suma
    return porcentaje

#Obtengo la matriz de covarianza de la matriz (imagen) transpuesta
def covarianceMatrixTranspose(A):
    return np.cov(A.T,rowvar=False)

#Normalizacion de la matriz
def centralizeRows(A):
    A_mean=np.zeros((1,A.shape[0]))
    for i in range(A.shape[0]):    
        A_mean[0][i]=np.mean(A[i,:])
    return np.subtract(A,A_mean.T),A_mean

#Ordeno los eigenvalores con sus respectivos eigenvectores
def ordenar(vectorComp,eigenVec,n):
    for i in range(n):
        for j in range(n-1):
            if(vectorComp[j]<vectorComp[j+1]):
                temp=vectorComp[j]
                vectorComp[j]=vectorComp[j+1]
                vectorComp[j+1]=temp
                temp=np.copy(eigenVec[:,j])
                eigenVec[:,j]=eigenVec[:,j+1]
                eigenVec[:,j+1]=temp
    return vectorComp,eigenVec

#Recupero la imágen con las componentes principales
def recoverImage(A,A_mean):
    for i in range(A.shape[0]):
        A[i]=A[i]+A_mean[0][i]
    return A


#Funcion para calcular el numero de componentes necesarios para llegar a la 
#varianza deseada. Así como también, retorno de variables útiles para la
#comparación de métodos en la compresión de imágenes
def calcComp(porcentajes,p):
    suma=.0
    pos=0
    var=[]
    for i in range(porcentajes.shape[0]):
        suma+=porcentajes[i]
        var.append(suma)
        if(suma>=p):
            pos=i
            break
    return pos,suma,var

def PCAmethod(A,p):
    #Normalizacion de la matrix
    B,A_mean=centralizeRows(A)
    #Covarianza de la matriz transpuesta
    C=covarianceMatrixTranspose(B)
    #error relativo mínimo para terminar de buscar los autovalores
    #con sus respectivos autovectores
    e=1.e-12
    x0=np.ones((C.shape[0],1),dtype=float) 
    #variable para almacenar los autovectores
    y_ss=np.zeros((C.shape[0],C.shape[1]),dtype=float)
    #Variable para almacenar los autovalores
    lambdas=np.zeros((1,C.shape[1]),dtype=float) 
    it=0
    #Encontrar los eigenvalores y eigenvectores
    while(it<C.shape[0]):
        lambdas[0,it],k,y_k,C=metodoPotencia(e,x0,C)
        y_ss[:,it]=y_k.T
        it=it+1
    #Ordenar los eigenvalores con sus respectivos eigenvectores
    lambdas,y_ss=ordenar(lambdas[0],y_ss,lambdas.shape[1])
    #Obtengo los porcentajes de varianza que cada componente aporta 
    percent=varianzaAportada(lambdas)
    #Obtengo la suma de porcentajes, numero de componentes necesarias
    #y la suma ascendete de la varianza en funcion de las componentes prncipales
    n,ss,var=calcComp(percent,p)
    U=np.copy(y_ss[:,0:n].T)
    Y=np.dot(U,B)
    #recuperación de la imagen
    A_=np.dot(U.T,Y)
    A_=recoverImage(A_,A_mean)
    return A_,n,var
    
#Cargar imagen. Solo se acepta de tipo uint8
img = mpimg.imread('alan.jpg')
#Imprimo el numero de filas, columnas y canales(si la imagen es a color)
print('***** PROPIEDADES DE LA IMAGEN *****')
print(img.shape, img.dtype)
print('************************************')
#Muestro la imagen en consola
plt.figure(figsize=(20,10))
plt.subplot('231')
plt.title('Imagen original')
plt.imshow(img)
#Hago un reshape de la imagen para tener una matriz mxn para poder trabajarlo
#1er parametro= objeto al que voy hacer el reshape
#2do parametro= los valores del newshape 
img_r = np.reshape(img, (img.shape[0],img.shape[1]*img.shape[2]))#.astype(np.float)
#Variar N entre [0,1]
N = 0.9
A_,n,var=PCAmethod(img_r,N)
A_=np.reshape(A_, (img.shape[0],img.shape[1],img.shape[2]))
plt.subplot('232')
plt.title('Método de la potencia')
plt.imshow(np.uint8(A_))
print('\n***** METODO DE LA POTENCIA *****')
print('Numero de componentes: ',n)
print('Porcentaje acumulado: ',var[len(var)-1])

#IMPLEMENTACIÓN CON LA LIBRERÍA scikit learn
print('\n***** SCIKIT LEARN *****')
pca = PCA(N).fit(img_r) 
print('Numero de componentes scikit learn: ',len(pca.explained_variance_ratio_),'\nPorcentaje acumulado: ', np.sum(pca.explained_variance_ratio_))
img_transformed = pca.transform(img_r) 
temp = pca.inverse_transform(img_transformed) 
temp = np.reshape(temp, (img.shape[0],img.shape[1],img.shape[2]))  
plt.subplot('233')
plt.title('Scikit learn')
plt.imshow(np.uint8(temp))
plt.savefig('PCA')
#Comparación de la varianza
plt.subplot('235')
plt.plot(np.cumsum(pca.explained_variance_ratio_))
plt.plot(range(0,len(var)),var)
plt.xlabel('Número de componentes')
plt.ylabel('Varianza explicativa acumulativa');