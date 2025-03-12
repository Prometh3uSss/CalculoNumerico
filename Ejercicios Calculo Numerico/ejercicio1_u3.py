import numpy as np
import matplotlib.pyplot as plt

class MatrizCondicion:
    def __init__(self, tamaños):
       #Inicializa la clase con los tamaños de las matrices que se van a generar
       # #tamaños: Un iterable que contiene los tamaños de las matrices (n x n)
        
        self.tamaños = tamaños
        self.condiciones = []

    def calcular_numero_condicion(self, matriz):
    
        #calcula el numero de condicion de una matriz dada

        #matriz: La matriz para la cual se calculará el numero de condicion
        #return: El numeroo de condicion de la matriz
        
        # Se obtienen los valores singulares de la matriz
        valores_singular = np.linalg.svd(matriz, compute_uv=False)
        # El numero de condicion se calcula como el cociente del mayor y el menor valor singular
        return valores_singular[0] / valores_singular[-1]

    def generar_matrices_y_calcular_condicion(self):
        
        #genera matrices aleatorias y calcula su numero de condicion
        #Los resultados se almacenan en la lista de condiciones
       
        for n in self.tamaños:
            # Genera una matriz aleatoria de tamaño n x n
            matriz = np.random.rand(n, n)
            # Calcula el numero de condicion de la matriz generada
            cond = self.calcular_numero_condicion(matriz)
            # Almacena el numero de condicion en la lista
            self.condiciones.append(cond)

    def visualizar_condicion(self):
        
        #Visualiza el numero de condicion en funcion del tamaño de lamatriz
        #Se genera un grafico que muestra como varia el numero de condicion con el tamaño de la matriz
        
        plt.figure(figsize=(10, 6))
        plt.plot(self.tamaños, self.condiciones, marker='o')
        plt.title('Numero de Condicion en Funcion del Tamaño de la Matriz')
        plt.xlabel('Tamaño de la Matriz (n x n)')
        plt.ylabel('Numero de Condicion')
        plt.grid()
        plt.xticks(self.tamaños)
        plt.yscale('log')  # Escala logaritmica para el eje y
        plt.show()


tamaños = range(2, 11)  
matriz_condicion = MatrizCondicion(tamaños)
matriz_condicion.generar_matrices_y_calcular_condicion()
matriz_condicion.visualizar_condicion()