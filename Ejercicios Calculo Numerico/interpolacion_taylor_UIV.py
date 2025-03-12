#Interpolacion de Taylor
import numpy as np
import matplotlib.pyplot as plt

class InterpolacionTemperatura:
    def __init__(self, dias, temperaturas):
        self.dias = dias
        self.temperaturas = temperaturas

    def interpolacion_taylor(self, x, orden=2):
        idx = np.argmin(np.abs(self.dias - x))
        valor_interpolado = self.temperaturas[idx]
        #Se calcula el valor interpolado usando el polinomio de Taylor
        for n in range(1, orden + 1):
            derivada = self.derivada(idx, n)
            valor_interpolado += (derivada / np.math.factorial(n)) * (x - self.dias[idx]) ** n
        return valor_interpolado

    def derivada(self, idx, orden):
        if orden == 0:
            return self.temperaturas[idx]
        elif orden == 1:
            return (self.temperaturas[min(idx + 1, len(self.temperaturas) - 1)] - 
                    self.temperaturas[max(idx - 1, 0)]) / 2
        elif orden == 2:
            return (self.temperaturas[min(idx + 1, len(self.temperaturas) - 1)] - 
                    2 * self.temperaturas[idx] + 
                    self.temperaturas[max(idx - 1, 0)]) 
        else:
            print("Advertencia: El Orden de derivada no es soportado. Se retorna 0.")
            return 0

#Datos de prueba:
dias = np.array([0, 1, 2, 3, 4, 5, 6])
temperaturas = np.array([20, 22, 21, 23, 24, 22, 20])

interp_temp = InterpolacionTemperatura(dias, temperaturas)

valores_x = np.linspace(0, 6, 100)#Se generan valores para la interpolacion
valores_y = []
for x in valores_x:
    valor_interpolado = interp_temp.interpolacion_taylor(x, orden=2)
    valores_y.append(valor_interpolado)

#Grafica
plt.figure(figsize=(10, 6))
plt.plot(dias, temperaturas,"o", label="Datos originales", color="blue")#Puntos originales
plt.plot(valores_x, valores_y, label="Interpolación de Taylor (Orden 2)", color="orange")#Curva de interpolacion
plt.title("Interpolación de Taylor de temperaturas diarias")
plt.xlabel("Días de la semana")
plt.ylabel("temperatura (°C)")
plt.legend()
plt.grid()
plt.show()
