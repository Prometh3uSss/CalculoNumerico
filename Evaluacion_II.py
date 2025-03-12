import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

# Clase para generar y almacenar datos meteorológicos
class DataGenerator:
    def __init__(self, days=7):
        self.days = np.arange(days)  # Días 0-6
        self.temperatures = self._generate_temperatures()
        self.derivatives = self._compute_derivatives()
    
    # Genera temperaturas simuladas usando una función senoidal con ruido
    def _generate_temperatures(self):
        x = self.days
        return 20 + 5 * np.sin(2 * np.pi * x / 7) + np.random.normal(0, 1, len(x))
    
    # Calcula derivadas usando diferencias finitas
    def _compute_derivatives(self):
        y = self.temperatures
        dy = np.zeros_like(y)
        n = len(y)
        for i in range(n):
            if i == 0:
                dy[i] = (y[i+1] - y[i])/1  # Diferencia hacia adelante
            elif i == n-1:
                dy[i] = (y[i] - y[i-1])/1  # Diferencia hacia atrás
            else:
                dy[i] = (y[i+1] - y[i-1])/2  # Diferencia central
        return dy

# Clase base para interpolación
class InterpolationMethod:
    def __init__(self, data):
        self.x = data.days
        self.y = data.temperatures
        self.dy = data.derivatives
    
    def plot(self, x_vals, y_vals, title):
        plt.scatter(self.x, self.y, color='red', label='Datos originales')
        plt.plot(x_vals, y_vals, label='Interpolación')
        plt.title(title)
        plt.legend()
        plt.show()

# Interpolación de Taylor (alrededor del punto medio)
class TaylorInterpolation(InterpolationMethod):
    def __init__(self, data, order=3):
        super().__init__(data)
        self.x0 = np.median(self.x)  # Punto medio (día 3)
        self.order = order
        self.coefficients = self._compute_coefficients()
    
    def _compute_coefficients(self):
        h = 1  # Espaciado diario
        derivatives = [self.y[np.where(self.x == self.x0)[0][0]]]
        
        # Calcula derivadas usando diferencias finitas centradas
        for i in range(1, self.order+1):
            idx = int(self.x0)
            if idx - i < 0 or idx + i >= len(self.x):
                break
            deriv = (self.y[idx + i] - self.y[idx - i]) / (2**i * h**i * np.math.factorial(i))
            derivatives.append(deriv)
        
        return derivatives
    
    def interpolate(self, x_vals):
        result = np.zeros_like(x_vals)
        for n in range(len(self.coefficients)):
            term = self.coefficients[n] * (x_vals - self.x0)**n
            result += term
        return result

# Interpolación de Lagrange
class LagrangeInterpolation(InterpolationMethod):
    def interpolate(self, x_vals):
        n = len(self.x)
        result = 0.0
        for i in range(n):
            term = self.y[i]
            for j in range(n):
                if i != j:
                    term *= (x_vals - self.x[j]) / (self.x[i] - self.x[j])
            result += term
        return result

# Interpolación de Hermite
class HermiteInterpolation(InterpolationMethod):
    def interpolate(self, x_vals):
        # Implementación básica usando splines cúbicos de SciPy con derivadas
        cs = CubicSpline(self.x, self.y, bc_type=((1, self.dy[0]), (1, self.dy[-1])))
        return cs(x_vals)

# Interpolación Polinómica a Trozos (Cubic Spline)
class PiecewisePolynomialInterpolation(InterpolationMethod):
    def interpolate(self, x_vals):
        cs = CubicSpline(self.x, self.y)
        return cs(x_vals)

# Generación de datos
data = DataGenerator()

# Crear interpoladores y graficar
x_vals = np.linspace(0, 6, 100)

# Taylor
taylor = TaylorInterpolation(data)
y_taylor = taylor.interpolate(x_vals)
taylor.plot(x_vals, y_taylor, "Interpolación de Taylor")

# Lagrange
lagrange = LagrangeInterpolation(data)
y_lagrange = lagrange.interpolate(x_vals)
lagrange.plot(x_vals, y_lagrange, "Interpolación de Lagrange")

# Hermite
hermite = HermiteInterpolation(data)
y_hermite = hermite.interpolate(x_vals)
hermite.plot(x_vals, y_hermite, "Interpolación de Hermite")

# Polinomio a trozos
piecewise = PiecewisePolynomialInterpolation(data)
y_piecewise = piecewise.interpolate(x_vals)
piecewise.plot(x_vals, y_piecewise, "Interpolación Polinómica a Trozos")