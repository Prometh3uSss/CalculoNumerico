from datetime import datetime

class Texto:
    def __init__(self, longitud_maxima):
        self.texto = ""
        self.longitud_maxima = longitud_maxima
        self.fecha_creacion = datetime.now()
        self.ultima_modificacion = self.fecha_creacion
def añadir_caracter_inicio(self, caracter):
    if len(self.texto) < self.longitud_maxima:
        self.texto = caracter + self.texto
        self.actualizar_ultima_modificacion
def añadir_caracter_final(self, caracter):
    if len(self.texto) < self.longitud_maxima:
        self.texto += caracter
        self.actualizar_ultima_modificacion
def añadir_cadena_inicio(self, cadena):
    if len(self.texto) + len(cadena) <= self.longitud_maxima:
        self.texto = cadena + self.texto
        self.actualizar_ultima_modificacion
def añadir_cadena_final(self, cadena):
    if len(self.texto) + len(cadena) <= self.longitud_maxima:
        self.texto += cadena
        self.actualizar_ultima_modificacion
def actualizar_ultima_modificacion(self):
    self.ultima_modificacion = datetime.now

def imprimir_informacion(self):
    print("Texto:", self.texto)
    print("Fecha de creación:", self.fecha_creacion)
    print("Última modificación:", self.ultima_modificacion)

# Ejemplo de uso
texto_prueba = Texto(20)
texto_prueba.añadir_caracter_inicio('H')
texto_prueba.añadir_cadena_final('ola')
texto_prueba.imprimir_informacion()