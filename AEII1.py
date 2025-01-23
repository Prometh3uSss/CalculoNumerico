def calcular_media():
    suma = 0
    contador = 0

    while True:
        try:
            numero = float(input("Ingrese un número positivo (0 para terminar): "))
            
            if numero < 0:
                print("Por favor, ingrese solo números positivos.")
                continue
            
            if numero == 0:
                break
            
            suma += numero
            contador += 1

        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")

    if contador == 0:
        print("No se ingresaron números positivos.")
    else:
        media = suma / contador
        print(f"La media de los números ingresados es: {media:.2f}")

# Llamar a la función para ejecutar el programa
calcular_media()