#Interpolacion de Lagrange
import numpy as np
import matplotlib.pyplot as plt

class InterpolacionTemperatura:
    def __init__(self, dias, temperaturas):
        self.dias = dias
        self.temperaturas = temperaturas

    def interpolacion_lagrange(self, x):
        n = len(self.dias)
        valor_interpolado = 0.0
        
        #Se calcula el valor interpolado usando el polinomio de Lagrange
        for i in range(n):
            termino = self.temperaturas[i]
            for j in range(n):
                if j != i:
                    #Multiplicacion por el termino de Lagrange
                    termino *= (x - self.dias[j]) / (self.dias[i] - self.dias[j])
            valor_interpolado += termino
        return valor_interpolado

#Datos de prueba:
dias = np.array([0, 1, 2, 3, 4, 5, 6])
temperaturas = np.array([20, 22, 21, 23, 24, 22, 20])

interp_temp = InterpolacionTemperatura(dias, temperaturas)

valores_x = np.linspace(0, 6, 100)#Se Generan valores para la interpolacion
valores_y = []
for x in valores_x:
    valor_interpolado = interp_temp.interpolacion_lagrange(x)
    valores_y.append(valor_interpolado)

#Grafica
plt.figure(figsize=(10, 6))
plt.plot(dias, temperaturas, "o", label="Datos Originales", color='blue')#Puntos originales
plt.plot(valores_x, valores_y, label="Interpolación de Lagrange", color="orange")#Curva de interpolacion
plt.title("Interpolacion de Lagrange de temperaturas diarias")
plt.xlabel("Días de la semana")
plt.ylabel("Temperatura (°C)")
plt.legend()
plt.grid()
plt.show()
