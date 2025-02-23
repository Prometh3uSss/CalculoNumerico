#Norma de Vector y Matriz como distancias en 3 Dimensiones

#Norma como distancias, error
#o distancia entre dos puntos
#caso 3D

import numpy as np

#Ingreso

x0 = np.array([0.0, 0, 0])
x1 = np.array([1, 2, 3], dtype=float)
x2 = np.array([2, 4, -1], dtype=float)

#Procedimiento

errado = x2 - x1
distancia = np.sqrt(np.sum(errado**2))

#Salida
print(errado)
print(distancia)

#Grafica
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

figura =plt.figure()
grafica = figura.add_subplot(111,projection='3d')

#Punto en el Espacio
[x, y, z] = x0
grafica.scatter(x,y,z, c='blue',
                marker = 'o', label = 'x0')

[x, y, z] = x1
grafica.scatter(x,y,z, c='red',
                marker = 'o', label = 'x1')

[x, y, z] = x2
grafica.scatter(x,y,z, c='green',
                marker = 'o', label = 'x2')

linea = np.concatenate(([x0], [x1]), axis=0)
print(linea)
x= linea[:,0]
y= linea[:,1]
z= linea[:,2]
grafica.plot(x,y,z, label='||x1||')

linea = np.concatenate(([x0], [x2]), axis=0)
print(linea)
x= linea[:,0]
y= linea[:,1]
z= linea[:,2]
grafica.plot(x,y,z, label='||x2||')

linea = np.concatenate(([x1], [x2]), axis=0)
print(linea)
x= linea[:,0]
y= linea[:,1]
z= linea[:,2]
grafica.plot(x,y,z, label='||error||')

grafica.set_xlabel('eje x')
grafica.set_ylabel('eje y')
grafica.set_zlabel('eje z')
grafica.legend()
grafica.view_init(35, 25)
plt.show()
