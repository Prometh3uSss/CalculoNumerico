import numpy as np
import matplotlib.pyplot as plt

class MetodoPotencia:
    def __init__(self, matriz, num_iteraciones=100, tolerancia=1e-10):
        
        #Inicializa la clase con la matriz, el numero de iteraciones y la tolerancia.

        #matriz: La matriz cuadrada de la que se desea calcular el autovalor y autovector
        #num_iteraciones: Numero maximo de iteraciones para el metodo
        #tolerancia: Tolerancia para determinar la convergenciaa
        
        self.matriz = matriz
        self.num_iteraciones = num_iteraciones
        self.tolerancia = tolerancia
        self.autovalores = []
        self.autovectores = []

    def calcular_autovalor_y_autovector(self):
        
        #calcula el autovalor dominante y el autovector asociado utilizando el metodo de potencia
        
        n = self.matriz.shape[0]  #obtener el tamano de la matriz
        #inicializar un vector aleatorio y normalizarlo
        b_k = np.random.rand(n)  
        b_k = b_k / np.linalg.norm(b_k)  

        for _ in range(self.num_iteraciones):
            #Multiplicar la matriz por el vector
            b_k_nuevo = np.dot(self.matriz, b_k)

            #Calcular el autovalor usando el producto escalar
            autovalor = np.dot(b_k_nuevo, b_k) / np.dot(b_k, b_k)
            self.autovalores.append(autovalor)

            #Normalizar el nuevo vector
            b_k_nuevo = b_k_nuevo / np.linalg.norm(b_k_nuevo)

            #Verificar la convergencia
            if np.linalg.norm(b_k_nuevo - b_k) < self.tolerancia:
                break

            #Actualizar el vector para la siguiente iteracion
            b_k = b_k_nuevo
            self.autovectores.append(b_k)

    def visualizar_convergencia(self):
        
        #Visualiza la convergencia del autovalor dominante a lo largo de las iteraciones
        
        plt.plot(self.autovalores, marker='o', linestyle='-', color='b')
        plt.xlabel('Iteracion')
        plt.ylabel('Autovalor dominante')
        plt.title('Convergencia del autovalor dominante')
        plt.grid(True)
        plt.show()

#definimos una matriz de ejemplo
A = np.array([[4, 1], [2, 3]])

#Creamos una instancia de la clase MetodoPotencia
metodo = MetodoPotencia(A)

#Llamamos al metodo para calcular autovalores y autovectores
metodo.calcular_autovalor_y_autovector()

print("Autovalor dominante estimado:", metodo.autovalores[-1])
print("Autovector asociado estimado:", metodo.autovectores[-1])
metodo.visualizar_convergencia()