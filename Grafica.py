import numpy as np
import matplotlib.pyplot as plt

# Generar un rango de valores de x
x = np.linspace(0, 2 * np.pi, 100)  # 100 puntos entre 0 y 2π

# Calcular los valores de y usando la función seno
y = np.sin(x)

# Crear la gráfica
plt.figure(figsize=(10, 5))  # Tamaño de la figura
plt.plot(x, y, label='Seno', color='blue')  # Graficar la función seno

# Añadir título y etiquetas
plt.title('Gráfica de la Función Seno')
plt.xlabel('x (radianes)')
plt.ylabel('sin(x)')

# Añadir una cuadrícula
plt.grid(True)

# Añadir una leyenda
plt.legend()

# Mostrar la gráfica
plt.show()