import numpy as np
import matplotlib.pyplot as plt

class FuncionMuestra:
    def __init__(self, inicio=0, fin=2*np.pi, num_puntos=10):
        self.x = np.linspace(inicio, fin, num_puntos)
        self.y = self._generar_funcion(self.x)
        self.dy = self._calcular_derivadas()
    
    def _generar_funcion(self, x):
        # Función base: sin(x) con ruido gaussiano
        return np.sin(x) + np.random.normal(0, 0.1, len(x))
    
    def _calcular_derivadas(self):
        # Calcula derivadas usando diferencias finitas
        derivadas = np.zeros_like(self.y)
        n = len(self.y)
        
        for i in range(n):
            if i == 0:
                # Diferencia hacia adelante
                derivadas[i] = (self.y[i+1] - self.y[i])/(self.x[i+1] - self.x[i])
            elif i == n-1:
                # Diferencia hacia atrás
                derivadas[i] = (self.y[i] - self.y[i-1])/(self.x[i] - self.x[i-1])
            else:
                # Diferencia central
                derivadas[i] = (self.y[i+1] - self.y[i-1])/(self.x[i+1] - self.x[i-1])
        return derivadas

class InterpoladorTaylor:
    def __init__(self, datos, x0, orden=3):
        self.datos = datos
        self.x0 = x0
        self.orden = orden
        self.coeficientes = self._calcular_coeficientes()
    
    def _indice_mas_cercano(self):
        return np.argmin(np.abs(self.datos.x - self.x0))
    
    def _calcular_coeficientes(self):
        idx = self._indice_mas_cercano()
        h = self.datos.x[1] - self.datos.x[0]  # Asume espaciado uniforme
        coeficientes = [self.datos.y[idx]]
        
        for n in range(1, self.orden+1):
            try:
                # Calcula derivada n-ésima usando diferencias finitas
                derivada = (self.datos.y[idx+n] - self.datos.y[idx-n]) / (2**n * h**n * np.math.factorial(n))
                coeficientes.append(derivada)
            except IndexError:
                break  # Ajusta el orden si no hay suficientes puntos
        return coeficientes
    
    def evaluar(self, x):
        resultado = 0.0
        for n, cn in enumerate(self.coeficientes):
            resultado += cn * (x - self.x0)**n
        return resultado
    
    def graficar(self):
        x_suave = np.linspace(min(self.datos.x), max(self.datos.x), 100)
        y_real = np.sin(x_suave)  # Función real sin ruido
        y_taylor = self.evaluar(x_suave)
        
        plt.figure(figsize=(10, 6))
        plt.scatter(self.datos.x, self.datos.y, color='red', label='Datos muestreados')
        plt.plot(x_suave, y_real, 'g--', label='Función real (sin ruido)')
        plt.plot(x_suave, y_taylor, 'b-', label=f'Taylor orden {len(self.coeficientes)-1}')
        plt.axvline(self.x0, color='purple', linestyle=':', label=f'Centro en x={self.x0:.2f}')
        plt.title('Aproximación de Taylor con Datos Muestreados')
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.legend()
        plt.grid(True)
        plt.show()

# Configuración y ejecución
if __name__ == "__main__":
    # Generar datos de muestra
    datos = FuncionMuestra(inicio=0, fin=2*np.pi, num_puntos=15)
    
    # Crear interpolador (usando π/2 como punto de expansión)
    taylor = InterpoladorTaylor(datos, x0=np.pi/2, orden=4)
    
    # Resultados
    print("Coeficientes del polinomio de Taylor:")
    for i, coef in enumerate(taylor.coeficientes):
        print(f"c{i} = {coef:.4f}")
    
    # Mostrar gráfica
    taylor.graficar()