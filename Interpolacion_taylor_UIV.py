import numpy as np
import matplotlib.pyplot as plt

class InterpolacionTaylor:
    def __init__(self, funcion, puntos, n):
        self.funcion = funcion
        self.puntos = puntos  # Lista de puntos alrededor de los cuales se expande
        self.n = n  # Grado del polinomio de Taylor

    def calcular_derivadas(self, a):
        """Calcula las derivadas de la función hasta el n-ésimo orden en el punto a."""
        derivadas = [self.funcion(a)]
        for i in range(1, self.n + 1):
            derivada = self.derivada(self.funcion, a, i)
            derivadas.append(derivada)
        return derivadas

    def derivada(self, f, x, n):
        """Calcula la n-ésima derivada de la función f en el punto x usando diferencias finitas."""
        h = 1e-5  # Paso pequeño
        if n == 0:
            return f(x)
        elif n == 1:
            return (f(x + h) - f(x - h)) / (2 * h)
        else:
            return (self.derivada(f, x + h, n - 1) - self.derivada(f, x - h, n - 1)) / (2 * h)

    def polinomio_taylor(self, x, a):
        """Calcula el polinomio de Taylor en el punto x alrededor de a."""
        derivadas = self.calcular_derivadas(a)
        P_n = 0
        for i in range(self.n + 1):
            P_n += (derivadas[i] / np.math.factorial(i)) * (x - a) ** i
        return P_n

    def graficar(self, x_range):
        """Grafica la función original y sus polinomios de Taylor en los puntos especificados."""
        x = np.linspace(x_range[0], x_range[1], 100)
        y_funcion = self.funcion(x)

        plt.plot(x, y_funcion, label='Función Original', color='blue')

        # Graficar el polinomio de Taylor para cada punto
        for a in self.puntos:
            y_taylor = [self.polinomio_taylor(xi, a) for xi in x]
            plt.plot(x, y_taylor, label=f'Polinomio de Taylor en x={a}', linestyle='--')

        plt.scatter(self.puntos, [self.funcion(a) for a in self.puntos], color='green', label='Puntos de Expansión')
        plt.legend()
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.title('Interpolación de Taylor')
        plt.grid()
        plt.show()

# Ejemplo de uso
def funcion_ejemplo(x):
    return np.sin(x)  # Función a interpolar

# Parámetros
puntos = [0, np.pi/4, np.pi/2]  # Puntos alrededor de los cuales se expande
n = 5  # Grado del polinomio de Taylor

# Crear objeto de interpolación
interpolador = InterpolacionTaylor(funcion_ejemplo, puntos, n)

# Graficar
interpolador.graficar((-2 * np.pi, 2 * np.pi))