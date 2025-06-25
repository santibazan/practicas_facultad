# Adivinar un número
# Generar un número aleatorio y dejar al usuario adivinar hasta acertar. Usar while
import random


numero_secreto = random.randint(1, 100)

print("Adivina el número secreto entre 1 y 100")

intento = None

while intento != numero_secreto:
    try:
        intento = int(input("Ingresa tu número: "))
        
        if intento < numero_secreto:
            print("Muy bajo. Intentalo de nuevo.")
        elif intento > numero_secreto:
            print("Muy alto. Intentalo de nuevo.")
        else:
            print(" Lo adivinaste!")
    except ValueError:
        print("Ingresa un numero valido.")
