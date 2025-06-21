# Crear un menú interactivo
# Mostrar opciones (1: saludar, 2: sumar, 3: salir) y usar while para repetir hasta salir
opcion=""
while opcion != "3":
    print("\nMenu:")
    print("1. Saludar")
    print("2. Sumar dos numeros")
    print("3. Salir")
    
    opcion = input("Ingrese una opcion: ")

    if opcion == "1":
        print("Hola ¿Como estas?")
    elif opcion == "2":
        try:
            num1 = int(input("Ingrese el primer numero: "))
            num2 = int(input("Ingrese el segundo numero: "))
            print(f"La suma es: {num1 + num2}")
        except ValueError:
            print("Por favor, ingrese numeros validos.")
    elif opcion == "3":
        print("Hasta pronto")
    else:
        print("Opcion invalida. Intente de nuevo.")