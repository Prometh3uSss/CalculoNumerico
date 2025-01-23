"""
class Demo:

    def __init__(self, cadena = ""):
        self.cadena = cadena

    def mostrar(self):
        print(self.cadena)

demo = Demo("Hola mundo")
demo.mostrar()
"""
"""
class Cancion:

    def __init__(self, titulo, artista, duracion):
        self.titulo = titulo
        self.artista = artista
        self.duracion = duracion

    def tocar(self):
        print(f"Se esta reproduciendo la cancion {self.titulo} de {self.artista} y su duracion es {self.duracion}")
    
    def pausar(self):
        print(f"Se pausa la cancion {self.titulo} de {self.artista}")

class Artista:

    def __init__(self, nombre = "", edad = 0, correo = ""):
        self.nombre = nombre
        self.edad = edad
        self.correo = correo
    
    def presentarse(self):
        print("Nombre: %s, Edad: %i" %(self.nombre, self.edad))

class Main:

    def __init__(self, listaCanciones):
        self.listaCanciones = listaCanciones

    def reproducir(self):
        for i in range(len(self.listaCanciones)):
            self.listaCanciones[i].tocar()
            self.listaCanciones[i].artista.presentar()

Artista = Artista["Boy", 24, "bad@gmail.com"]
Cancion = Cancion("Saludar", Artista, "18min")
listaCanciones = [Cancion]
Main = Main(listaCanciones)
Main.reproducir()

artista = Artista("Chino", 40, "chino@gmail.com")
cancion = Cancion("Danza Kuduro", "Don Omar", "3:45min")

cancion.tocar()
cancion.pausar()
artista.presentarse()
"""

#Modificado por BlackBox

class Cancion:
    def __init__(self, titulo, artista, duracion):
        self.titulo = titulo
        self.artista = artista
        self.duracion = duracion

    def tocar(self):
        print(f"Se está reproduciendo la canción '{self.titulo}' de {self.artista.nombre} y su duración es {self.duracion}")
    
    def pausar(self):
        print(f"Se pausa la canción '{self.titulo}' de {self.artista.nombre}")

class Artista:
    def __init__(self, nombre="", edad=0, correo=""):
        self.nombre = nombre
        self.edad = edad
        self.correo = correo
    
    def presentarse(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")

class Main:
    def __init__(self, listaCanciones):
        self.listaCanciones = listaCanciones

    def reproducir(self):
        for cancion in self.listaCanciones:
            cancion.tocar()
            cancion.artista.presentarse()

# Crear un artista
artista1 = Artista("Boy", 24, "bad@gmail.com")
# Crear una canción
cancion1 = Cancion("Saludar", artista1, "18 min")
# Crear una lista de canciones
listaCanciones = [cancion1]
# Crear la instancia de Main y reproducir
main = Main(listaCanciones)
main.reproducir()

# Crear otro artista y canción
artista2 = Artista("Chino", 40, "chino@gmail.com")
cancion2 = Cancion("Danza Kuduro", artista2, "3:45 min")

# Tocar y pausar la segunda canción
cancion2.tocar()
cancion2.pausar()
artista2.presentarse()