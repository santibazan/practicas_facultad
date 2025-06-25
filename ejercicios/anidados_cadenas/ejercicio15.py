# Determinar si un número es primo
# Usar un for para verificar si un número tiene solo 2 divisores
num = int(input("Ingrese un numero para saber si es primo: "))
primo=True
if num <= 1:
    primo = False
else:
    for i in range(2, num):
        if num % i == 0:
            primo = False
            break

if primo:
    print(f"El número {num} es primo")
else:
    print(f"El número {num} no es primo")