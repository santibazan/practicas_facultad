# Simular una contraseña
# Pedir contraseña al usuario y permitir 3 intentos
intentos = 3
contraseña = "UTN"
for i in range (3):
    password = input("Ingrese la contraseña: ")
    if password == contraseña:
        print("Ingreso valido")
        break
    else:
        print("Ingreso invalido.")
