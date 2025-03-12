import numpy as np
import matplotlib.pyplot as plt

class MatrizRigidez:
    def __init__(self, n):
        #Genera una matriz simetrica aleatoria y positiva definida
        self.n = n
        self.A = self.generar_matriz_rigidez()
    
    def generar_matriz_rigidez(self):
        A = np.random.rand(self.n, self.n)
        A = (A + A.T) / 2  #Hacerla simetrica
        A += self.n * np.eye(self.n)  #Aumentar la diagonal par asegurar que sea positiva definida
        return A
    
    def numero_condicion(self):
        autovalores = np.linalg.eigvalsh(self.A)
        lambda_max = np.max(autovalores)
        lambda_min = np.min(autovalores)
        return lambda_max / lambda_min

class AnalisisEstructural:
    def __init__(self, matriz_rigidez):
        self.A = matriz_rigidez.A
        self.n = matriz_rigidez.n
    
    def metodo_potencia(self, max_iter=1000, tol=1e-6):
        x = np.random.rand(self.n)
        x = x / np.linalg.norm(x)
        autovalores = []
        
        for _ in range(max_iter):
            x_nuevo = np.dot(self.A, x)
            x_nuevo = x_nuevo / np.linalg.norm(x_nuevo)
            autovalor = np.dot(x_nuevo.T, np.dot(self.A, x_nuevo))
            autovalores.append(autovalor)
            if np.linalg.norm(x_nuevo - x) < tol:
                break
            x = x_nuevo
        
        return autovalor, x_nuevo, autovalores

    def metodo_potencia_inverso(self, max_iter=1000, tol=1e-6):
        x = np.random.rand(self.n)
        x = x / np.linalg.norm(x)
        autovalores = []
        
        for _ in range(max_iter):
            #Resolvemos A * y=x
            y = np.linalg.solve(self.A, x)
            y = y / np.linalg.norm(y)
            autovalor = np.dot(y.T, np.dot(self.A, y))
            autovalores.append(autovalor)
            if np.linalg.norm(y - x) < tol:
                break
            x = y
        
        return 1/autovalor, y, autovalores  # Retornamos el inverso del autovalor

def main():
    n = 5  #Tamaño de la matriz
    matriz_rigidez = MatrizRigidez(n)
    
    print("Matriz de Rigidez A:")
    print(matriz_rigidez.A)
    
    # Calculo del numero de condicion
    condicion = matriz_rigidez.numero_condicion()
    print(f"Número de condición: {condicion}")
    
    #Analisis estructural
    analisis = AnalisisEstructural(matriz_rigidez)
    
    #Metodo de Potencia
    autovalor_max, vector_max, autovalores_max = analisis.metodo_potencia()
    print(f"Autovalor dominante: {autovalor_max}")
    print(f"Autovector correspondiente: {vector_max}")
    
    #Metodo de Potencia Inverso
    autovalor_min, vector_min, autovalores_min = analisis.metodo_potencia_inverso()
    print(f"Autovalor más pequeño: {autovalor_min}")
    print(f"Autovector correspondiente: {vector_min}")
    
    #Visualizacion de la convergencia
    plt.figure(figsize=(12, 6))
    
    plt.subplot(1, 2, 1)
    plt.plot(autovalores_max, label='Método de Potencia')
    plt.title('Convergencia del Método de Potencia')
    plt.xlabel('Iteraciones')
    plt.ylabel('Autovalor')
    plt.legend()
    
    plt.subplot(1, 2, 2)
    plt.plot(autovalores_min, label='Método de Potencia Inverso', color='orange')
    plt.title('Convergencia del Método de Potencia Inverso')
    plt.xlabel('Iteraciones')
    plt.ylabel('Autovalor')
    plt.legend()
    
    plt.tight_layout()
    plt.show()

main()