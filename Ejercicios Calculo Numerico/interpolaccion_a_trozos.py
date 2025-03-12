import numpy as np
import matplotlib.pyplot as plt

class InterpoladorLineal:
    def __init__(self, x, y):
        # x(dias), y(temperatura)
        self.x = x
        self.y = y
    def interpolar(self, valor_x):
        for i in range(len(self.x) - 1):
            if self.x[i] <= valor_x <= self.x[i + 1]:
                #ahora calculos las pendientes de los puntos (x[i], y[i]) y (x[i+1], y[i+1])
                pendiente = (self.y[i + 1] - self.y[i]) / (self.x[i + 1] - self.x[i])
                return self.y[i] + pendiente * (valor_x - self.x[i])
#colocaremos las variables con los datos de las temperaturas diarias
#x va a ser igual a los dias de la semana
x = np.array([0, 1, 2, 3, 4, 5, 6])
#y va a ser igual a las temperaturas en °c
y = np.array([15, 17, 16, 18, 20, 19, 21])
interpolador = InterpoladorLineal(x, y)
x_grafica = np.linspace(0, 6, 100)
y_grafica = [interpolador.interpolar(valor) for valor in x_grafica]
#vamos a configurar la gráfica, lo aprendi en este video: https://www.youtube.com/watch?v=on1JT_c3FRQ&ab_channel=Matem%C3%A1tica2Biolog%C3%ADa
plt.figure(figsize=(10, 6))
plt.plot(x, y, "ro", label="datos originales", markersize=8)
plt.plot(x_grafica, y_grafica, "b-", label="interpolación lineal a trozos", linewidth=2)
plt.title("interpolación lineal a trozos de temperaturas diarias", fontsize=14)
plt.xlabel("dias de la semana", fontsize=12)
plt.ylabel("temperatura (°c)", fontsize=12)
plt.xticks(x, ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"])
plt.grid(True, linestyle="--", alpha=0.7)
plt.legend(loc="upper left")
plt.show()