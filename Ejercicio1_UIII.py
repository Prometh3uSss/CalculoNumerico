import numpy as np
import matplotlib.pyplot as plt

def calcular_numero_condicion(matriz):
    """
    Calcula el número de condición de una matriz.
    
    Args:
    matriz (np.ndarray): La matriz para la cual se calculará el número de condición.
    
    Returns:
    float: El número de condición de la matriz.
    """
    # Calcular el valor singular máximo y mínimo
    valores_singulares = np.linalg.svd(matriz, compute_uv=False)
    condicion = valores_singulares[0] / valores_singulares[-1]
    return condicion

def generar_matrices_y_calcular_condicion(tamaños):
    """
    Genera matrices aleatorias y calcula su número de condición.
    
    Args:
    tamaños (list): Lista de tamaños de matrices a generar.
    
    Returns:
    list: Lista de números de condición correspondientes a cada tamaño de matriz.
    """
    numeros_condicion = []
    for n in tamaños:
        matriz = np.random.rand(n, n)  # Generar matriz aleatoria de tamaño n x n
        condicion = calcular_numero_condicion(matriz)
        numeros_condicion.append(condicion)
    return numeros_condicion

def visualizar_condicion(tamaños, numeros_condicion):
    """
    Visualiza el número de condición en función del tamaño de la matriz.
    
    Args:
    tamaños (list): Lista de tamaños de matrices.
    numeros_condicion (list): Lista de números de condición correspondientes.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(tamaños, numeros_condicion, marker='o')
    plt.title('Número de Condición en Función del Tamaño de la Matriz')
    plt.xlabel('Tamaño de la Matriz (n x n)')
    plt.ylabel('Número de Condición')
    plt.grid()
    plt.xticks(tamaños)
    plt.yscale('log')  # Usar escala logarítmica para mejor visualización
    plt.show()

# Definir los tamaños de las matrices a generar
tamaños = list(range(3, 11))  # Matrices de 3x3 a 10x10

# Generar matrices y calcular el número de condición
numeros_condicion = generar_matrices_y_calcular_condicion(tamaños)

# Visualizar el resultado
visualizar_condicion(tamaños, numeros_condicion)