import numpy as np
import matplotlib.pyplot as plt

class MatrizCovarianza:
    def __init__(self, n_activos):
        self.n_activos = n_activos
        self.C = self.generar_matriz_covarianza()

    def generar_matriz_covarianza(self):
        #generar una matriz aleatoria y calcular la matriz de covarianza
        A = np.random.rand(self.n_activos, self.n_activos)
        return np.dot(A.T, A)

    def numero_condicion(self):
        #Calcular  autovalores
        autovalores = np.linalg.eigvalsh(self.C)
        lambda_max = np.max(autovalores)
        lambda_min = np.min(autovalores)
        return lambda_max / lambda_min

class MetodoPotencia:
    def __init__(self, matriz_covarianza):
        self.C = matriz_covarianza
        self.autovalores = []

    def autovalor_dominante(self, num_iteraciones=1000, tolerancia=1e-10):
        n = self.C.shape[0]
        b_k = np.random.rand(n)
        b_k = b_k / np.linalg.norm(b_k)

        for _ in range(num_iteraciones):
            b_k1 = np.dot(self.C, b_k)
            b_k1_norm = np.linalg.norm(b_k1)
            b_k1 = b_k1 / b_k1_norm

            #Calcular elautovalor
            lambda_k = np.dot(b_k1.T, np.dot(self.C, b_k1)) / np.dot(b_k1.T, b_k1)
            self.autovalores.append(lambda_k)

            if np.linalg.norm(b_k1 - b_k) < tolerancia:
                break

            b_k = b_k1

        return lambda_k, b_k1

class MetodoPotenciaInverso:
    def __init__(self, matriz_covarianza):
        self.C = matriz_covarianza
        self.autovalores = []

    def autovalor_mas_pequeno(self, num_iteraciones=1000, tolerancia=1e-10):
        n = self.C.shape[0]
        b_k = np.random.rand(n)
        b_k = b_k / np.linalg.norm(b_k)

        for _ in range(num_iteraciones):
            #Resolver C x =b_k
            x = np.linalg.solve(self.C, b_k)
            x_norm = np.linalg.norm(x)
            b_k1 = x / x_norm

            #Calcular el autovalor
            lambda_k = np.dot(b_k1.T, np.dot(self.C, b_k1)) / np.dot(b_k1.T, b_k1)
            self.autovalores.append(1 / lambda_k)  # Guardar el autovalor invertido

            if np.linalg.norm(b_k1 - b_k) < tolerancia:
                break

            b_k = b_k1

        return 1 / lambda_k, b_k1

def main():
    n_activos = 5  #numero de activos
    matriz_covarianza = MatrizCovarianza(n_activos)

    # Calculo del número de condición
    numero_condicion = matriz_covarianza.numero_condicion()
    print("Número de Condicion:", numero_condicion)

    #Metodo de Potencia
    metodo_potencia = MetodoPotencia(matriz_covarianza.C)
    lambda_dominante, autovector_dominante = metodo_potencia.autovalor_dominante()
    print("Autovalor Dominante:", lambda_dominante)
    print("Autovector Asociado:", autovector_dominante)

    #Metodo de Potencia Inverso
    metodo_potencia_inverso = MetodoPotenciaInverso(matriz_covarianza.C)
    lambda_mas_pequeno, autovector_mas_pequeno = metodo_potencia_inverso.autovalor_mas_pequeno()
    print("Autovalor Más Pequeño:", lambda_mas_pequeno)
    print("Autovector Asociado:", autovector_mas_pequeno)

    # Visualizacion de la convergencia
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.plot(metodo_potencia.autovalores, label='Autovalores Dominantes')
    plt.title('Convergencia del Método de Potencia')
    plt.xlabel('Iteraciones')
    plt.ylabel('Autovalor')
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.plot(metodo_potencia_inverso.autovalores, label='Autovalores Inversos', color='orange')
    plt.title('Convergencia del Método de Potencia Inverso')
    plt.xlabel('Iteraciones')
    plt.ylabel('Autovalor')
    plt.legend()

    plt.tight_layout()
    plt.show()


main()