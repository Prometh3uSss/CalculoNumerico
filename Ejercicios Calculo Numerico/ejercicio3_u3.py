import numpy as np
import matplotlib.pyplot as plt

class MetodoPotenciaSimetrico:
    def __init__(self, matriz, num_iteraciones=100, tolerancia=1e-10):
        
        #empezamos la clase con la matriz, el numero de iteraciones y la tolerancia

        #matriz: La matriz cuadrada de la que se desea calcular el autovalor y autovector
        #num_iteraciones: Numero maximo de iteraciones para el metodo
        #tolerancia: Tolerancia para determinar la convergencia
        
        self.matriz = matriz
        self.num_iteraciones = num_iteraciones
        self.tolerancia = tolerancia
        self.autovalores = []  # Aqui guarda los autovalores calculados
        self.autovectores = []  # Aqui guarda los autovectores calculados

    def calcular_autovalor_y_autovector(self):
        
        #este metodo calcula el autovalor dominante y el autovector asociado
        #utilizando el metodo de potencia simetrico
        
        n = self.matriz.shape[0]  #Obtenemos el tamaño de la matriz
        #Comenzamos con un vector aleatorio y lo normalizamos
        b_k = np.random.rand(n)  
        b_k = b_k / np.linalg.norm(b_k)  

        #Realizamos el calculo durante el numero de iteraciones especificado
        for _ in range(self.num_iteraciones):
            #Multiplicamos la matriz por el vector
            b_k_nuevo = np.dot(self.matriz, b_k)

            #Calcula el autovalor usando el producto escalar
            autovalor = np.dot(b_k_nuevo, b_k) / np.dot(b_k, b_k)
            self.autovalores.append(autovalor)  # Guardamos el autovalor

            #Normalizamos el nuevo vector
            b_k_nuevo = b_k_nuevo / np.linalg.norm(b_k_nuevo)

            #Comprobamos si hemos alcanzado la convergencia
            if np.linalg.norm(b_k_nuevo - b_k) < self.tolerancia:
                print("Convergencia alcanzada despues de", len(self.autovalores), "iteraciones.")
                break

            #Actualizamos el vector para la siguiente iteracion
            b_k = b_k_nuevo
            self.autovectores.append(b_k)  #Guarda el autovector

    def visualizar_convergencia(self):
        
        #Este metodo visualizacomo el autovalor y el autovector dominante
        #convergen alo largo de las iteraciones
        
        plt.figure(figsize=(12, 5))

        #Graficamos la convergencia del autovalor
        plt.subplot(1, 2, 1)
        plt.plot(self.autovalores, marker='o', linestyle='-', color='b')
        plt.xlabel('Iteracion')
        plt.ylabel('Autovalor dominante')
        plt.title('Convergencia del autovalor dominante')
        plt.grid(True)

        #Graficamos la convergencia de la primera componente delautovector
        plt.subplot(1, 2, 2)
        primera_componente = [v[0] for v in self.autovectores] 
        plt.plot(primera_componente, marker='o', linestyle='-', color='r')
        plt.xlabel('Iteracion')
        plt.ylabel('Primera componente del autovector')
        plt.title('Convergencia del autovector dominante')
        plt.grid(True)

        plt.tight_layout()  #Ajustamos el diseño para que no se superpongan
        plt.show()  #Mostramos las graficas

#Definimos una matriz de ejemplo
A = np.array([[4, 1], [1, 3]])

#creamos una instancia de la clase MetodoPotenciaSimetrico
metodo = MetodoPotenciaSimetrico(A)

#Llamamos al metodo para calcular autovalores y autovectores
metodo.calcular_autovalor_y_autovector()

print("Autovalor dominante estimado:", metodo.autovalores[-1])
print("Autovector asociado estimado:", metodo.autovectores[-1])

#Visualizamos la convergencia
metodo.visualizar_convergencia()