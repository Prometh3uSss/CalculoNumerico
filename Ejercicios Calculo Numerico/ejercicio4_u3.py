import numpy as np
import matplotlib.pyplot as plt

class MetodoPotenciaInverso:
    def __init__(self, matriz, num_iteraciones=100, tolerancia=1e-10):
        
        #Inicializa la clase con la matriz el numero de iteraciones y la tolerancia

        #matriz: Lamatriz cuadrada de la que se desea calcular el autovalor y autovector
        #num_iteraciones: numero maximo de iteraciones para el metodo
        #tolerancia: Tolerancia para determinar la convergencia
        
        self.matriz = matriz
        self.num_iteraciones = num_iteraciones
        self.tolerancia = tolerancia
        self.autovalores = []  #aqui guarda los autovalores calculados
        self.autovectores = []  #aqui guardaremos los autovectores calculados

    def calcular_autovalor_y_autovector(self):
        
        #Este metodo calcula el autovalor mas pequeño y el autovector asociado
        #utilizando el metodo de potencia inverso
        
        n = self.matriz.shape[0]  #obtenemos el tamaño de la matriz
        #Comenzamos con un vector aleatorio y lo normalizamos
        b_k = np.random.rand(n)  
        b_k = b_k / np.linalg.norm(b_k)  

        #Realizamos el calculo durante el numero de iteraciones especificado
        for i in range(self.num_iteraciones):
            #Resolvemos el sistema de ecuaciones (A * b_k_nuevo = b_k)
            b_k_nuevo = np.linalg.solve(self.matriz, b_k)

            #Calculamos el autovalor usando el producto escalar
            autovalor = np.dot(b_k, b_k) / np.dot(b_k_nuevo, b_k_nuevo)
            self.autovalores.append(autovalor)  # Guardamos el autovalor

            #Normalizamos el nuevo vector
            b_k_nuevo = b_k_nuevo / np.linalg.norm(b_k_nuevo)

            # Comprobamos si hemos alcanzado la convergencia
            if np.linalg.norm(b_k_nuevo - b_k) < self.tolerancia:
                print(f"Convergencia alcanzada en la iteracion {i + 1}.")
                break

            #Actualizamos el vector para la siguiente iteracion
            b_k = b_k_nuevo
            self.autovectores.append(b_k)  # Guarda el autovector

    def visualizar_convergencia(self):
        
        #este metodo visualiza como el autovalor mas pequeño converge a lo largo de las iteraciones.
        
        plt.figure(figsize=(10, 5))
        plt.plot(self.autovalores, marker='o', linestyle='-', color='b')
        plt.xlabel('Iteracion')
        plt.ylabel('Autovalor mas pequeño')
        plt.title('Convergencia del autovalor mas pequeño')
        plt.grid(True)
        plt.show()

#Definimos una matriz de ejemplo
A = np.array([[4, 1], [1, 3]])

#Creamos una instancia de la clase MetodoPotenciaInverso
metodo = MetodoPotenciaInverso(A)

#Llamamos al metodo para calcular autovalores y autovectores
metodo.calcular_autovalor_y_autovector()

print("Autovalor mas pequeno estimado:", metodo.autovalores[-1])
print("Autovector asociado estimado:", metodo.autovectores[-1])
metodo.visualizar_convergencia()