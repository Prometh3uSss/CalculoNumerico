import numpy as np
import matplotlib.pyplot as plt

class HermiteInterpolacion:
    def __init__(self, x, y, derivada):
        #x(dias), y(temperatura)
        self.x = x
        self.y = y
        self.derivada = derivada
        self.dif_div, self.x2 = self.diferencias_divididas_hermite()
    def diferencias_divididas_hermite(self):
        puntos_interpolacion = len(self.x)
        puntos_inter2 = np.zeros(2 * puntos_interpolacion)
        diferencias_div = np.zeros((2 * puntos_interpolacion, 2 * puntos_interpolacion))
        for i in range(puntos_interpolacion):
            puntos_inter2[2 * i] = self.x[i]
            puntos_inter2[2 * i + 1] = self.x[i]
            diferencias_div[2 * i][0] = self.y[i]
            diferencias_div[2 * i + 1][0] = self.y[i]
            diferencias_div[2 * i + 1][1] = self.derivada[i]
            if i != 0:
                diferencias_div[2 * i][1] = (diferencias_div[2 * i][0] - diferencias_div[2 * i - 1][0]) / (puntos_inter2[2 * i] - puntos_inter2[2 * i - 1])
        #ahora calculamos las diferencias divididas
        for i in range(2, 2 * puntos_interpolacion):
            for j in range(2, i + 1):
                diferencias_div[i][j] = (diferencias_div[i][j - 1] - diferencias_div[i - 1][j - 1]) / (puntos_inter2[i] - puntos_inter2[i - j])
        return diferencias_div, puntos_inter2
    def evaluar(self, valor):
        n = len(self.x2)
        resultado = self.dif_div[0][0]
        producto = 1  
        for i in range(1, n):
            producto *= (valor - self.x2[i - 1])
            resultado += self.dif_div[i][i] * producto
        return resultado
#colocaremos las variables con los datos de las temperaturas diarias
#x va a ser igual a los dias de la semana
x = np.array([0, 1, 2, 3, 4, 5, 6])
#y va a ser igual a las temperaturas en °c
y = np.array([15, 17, 16, 18, 20, 19, 21])
derivada = np.gradient(y, x)
#el punto que vamos a evaluar va a ser un día por ejemplo el día 3 (la salida tiene que ser 18)
punto = 3
# Se crea la instancia del interpolador de Hermite
hermite = HermiteInterpolacion(x, y, derivada)
valor_interpolado = hermite.evaluar(punto)
print(f"La temperatura interpolada en el dia {punto} es {valor_interpolado:.2f} °C")
#graficamos
x_vals = np.linspace(min(x), max(x), 100)
y_vals = [hermite.evaluar(val) for val in x_vals]
plt.plot(x_vals, y_vals, label="polinomio de hermite")
plt.scatter(x, y, color='red', label="temperaturas diarias")
plt.title("Interpolacion de Hermite para temperaturas diarias")
plt.xlabel("dia")
plt.ylabel("temperatura (°c)")
plt.legend()
plt.grid()
plt.show()