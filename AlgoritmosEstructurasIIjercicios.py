"""
def arearec (base,altura):
    aResult = (base * altura)
    return aResult

base = (int(input("Base: ")))
altura = (int(input("Altura: ")))
rAreaRec = arearec(base, altura)
print("El area del Rectangulo es: %i" %rAreaRec)
"""

"""
def arearec(base, altura):
    return base * altura


try:
    base = int(input("Base: "))
    altura = int(input("Altura: "))
    rAreaRec = arearec(base, altura)
    print(f"El área del rectángulo es: {rAreaRec}")
except ValueError:
    print("Por favor, ingrese valores numéricos válidos.")
"""

"""
def perrec (base, altura):
    pResult = 2 * (base + altura)
    return pResult

base = (int(input("Base: ")))
altura = (int(input("Altura: ")))
rPerRec = perrec(base, altura)
print(f"El perimetro del rectangulo es: {rPerRec}")
"""

listadatos = []

def alumno():
    return {
        "cedula": None,
        "nombre": None,
        "apellido": None,
        "correo": None,
        "nota": None
    }

# Crear un nuevo alumno
def crear():
    objeto = alumno()
    print("Insertar Alumno (no debe haber alumnos repetidos)")
    
    cedula = str(input("Cédula: "))
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    correo = input("Correo: ")
    
    try:
        nota = int(input("Nota: "))
    except ValueError:
        print("La nota debe ser un número entero.")
        return

    objeto["cedula"] = cedula
    objeto["nombre"] = nombre
    objeto["apellido"] = apellido
    objeto["correo"] = correo
    objeto["nota"] = nota

    existe = False
    for fila in listadatos:
        if fila["cedula"] == cedula:
            existe = True
            break

    if not existe:
        listadatos.append(objeto)
        print("Alumno agregado correctamente.")
    else:
        print("El alumno ya existe.")

# Listar todos los alumnos
def listar():
    print("Listar notas")
    print("Cédula Nombre Apellido Correo Nota")
    for fila in listadatos:
        print(" %s %s %s %s %i" % (fila["cedula"], fila["nombre"],
        fila["apellido"], fila["correo"], fila["nota"]))

# Consultar un alumno por cédula
def consultar():
    print("Consultar Notas según cédula")
    cedula = str(input("Cédula: "))
    encontrado = False
    for fila in listadatos:
        if fila["cedula"] == cedula:
            encontrado = True
            print("Alumno encontrado:")
            print("Cédula: %s" % fila["cedula"])
            print("Nombre: %s" % fila["nombre"])
            print("Apellido: %s" % fila["apellido"])
            print("Correo: %s" % fila["correo"])
            print("Nota: %s" % fila["nota"])
            break
    if not encontrado:
        print("Alumno no encontrado.")
    print("Terminado.")

# Eliminar un alumno por cédula
def eliminar():
    print("Eliminar Alumno según cédula introducida")
    cedula = str(input("Cédula: "))
    encontrado = False
    for fila in listadatos:
        if fila["cedula"] == cedula:
            listadatos.remove(fila)
            print("Alumno eliminado correctamente.")
            encontrado = True
            break
    if not encontrado:
        print("Alumno no encontrado.")
    print("Terminado.")

# Modificar los datos de un alumno
def modificar():
    print("Modificar datos del alumno según cédula introducida")
    cedula = str(input("Cédula: "))
    encontrado = False
    for fila in listadatos:
        if fila["cedula"] == cedula:
            encontrado = True
            print("Datos actuales del alumno:")
            print(" %s %s %s %s %i" % (fila["cedula"], fila["nombre"],
            fila["apellido"], fila["correo"], fila["nota"]))
            print("Introducir nuevos datos:")
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            correo = input("Correo: ")
            try:
                nota = int(input("Nota: "))
            except ValueError:
                print("La nota debe ser un número entero.")
                return
            
            fila["nombre "] = nombre
            fila["apellido"] = apellido
            fila["correo"] = correo
            fila["nota"] = nota
            print("Alumno modificado correctamente.")
            break
    if not encontrado:
        print("Alumno no encontrado.")
    print("Terminado.")

def main():
    eje = True
    print("--- Menú Principal ---")
    while eje:
        print("0.- Salir")
        print("1.- Insertar Nuevo Alumno")
        print("2.- Modificar Alumno según su cédula")
        print("3.- Eliminar Alumno según su cédula")
        print("4.- Consultar Alumno según su cédula")
        print("5.- Listar las notas de todos los alumnos existentes")
        try:
            comando = int(input("/> "))
        except ValueError:
            print("Por favor, ingrese un número válido.")
            continue

        if comando == 1:
            crear()
        elif comando == 2:
            modificar()
        elif comando == 3:
            eliminar()
        elif comando == 4:
            consultar()
        elif comando == 5:
            listar()
        elif comando == 0:
            eje = False
        else:
            print("Comando no válido. Intente de nuevo.")

    print("Programa finalizado correctamente.")

main()



