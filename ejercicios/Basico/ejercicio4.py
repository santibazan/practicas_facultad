# Tabla de multiplicar
# Pedir un número al usuario y mostrar su tabla de multiplicar del 1 al 10

num = int(input("Ingrese un numero para saber sus multiplicaciones hasta la tabla del 10: "))

for i in range(1,11):
    mult = num*i
    print(f"{num} x {i} = {mult}")