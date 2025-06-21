# Sumar números hasta que el usuario escriba 0
# Usar un while para pedir números y sumarlos, termina cuando se ingresa 0
suma = 0
num = 1
while num != 0:
    num = int(input("Ingrese un numero para luego hacer la suma de dichos numeros, para finalizar ingrese el 0: "))
    suma += num
print(suma)