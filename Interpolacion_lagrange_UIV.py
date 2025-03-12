import numpy as np
import matplotlib.pyplot as plt

class InterpolacionLagrange:
    def __init__(self, xi, fi):
        self.xi = np.array(xi)
        self.fi = np.array(fi)
        self.n = len(xi)

    def calcular_polinomio(self):
        def polinomio(x):
            total = 0
            for i in range(self.n):
                # Calcular el término de Lagrange
                numerador = 1
                denominador = 1
                for j in range(self.n):
                    if j != i:
                        numerador *= (x - self.xi[j])
                        denominador *= (self.xi[i] - self.xi[j])
                total += (numerador / denominador) * self.fi[i]
            return total
        return polinomio

    def graficar(self):
        # Crear el polinomio
        polinomio = self.calcular_polinomio()
        
        # Puntos para la gráfica
        muestras = 101
        a = np.min(self.xi)
        b = np.max(self.xi)
        pxi = np.linspace(a, b, muestras)
        pfi = np.array([polinomio(x) for x in pxi])

        # Gráfica
        plt.plot(self.xi, self.fi, 'o', label='Puntos')
        plt.plot(pxi, pfi, label='Polinomio')
        plt.legend()
        plt.xlabel('xi')
        plt.ylabel('fi')
        plt.title('Interpolación Lagrange')
        plt.grid()
        plt.show()

    def mostrar_resultados(self):
        divisorL = np.zeros(self.n, dtype=float)
        for i in range(self.n):
            denominador = 1
            for j in range(self.n):
                if j != i:
                    denominador *= (self.xi[i] - self.xi[j])
            divisorL[i] = denominador

        print('    valores de fi: ', self.fi)
        print('divisores en L(i): ', divisorL)

# INGRESO , Datos de prueba
xi = [0, 0.2, 0.3, 0.4, 0.5, 0.6]  # Añadir más puntos
fi = [1, 1.6, 1.7, 2.0, 2.2, 2.5]  # Valores correspondientes

# Crear objeto de interpolación
interpolador = InterpolacionLagrange(xi, fi)

# Mostrar resultados
interpolador.mostrar_resultados()

# Graficar
interpolador.graficar()