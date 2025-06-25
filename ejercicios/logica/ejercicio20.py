# Generar una pirámide numérica
# 1
# 1 2
# 1 2 3
# ...
filas = int(input("Ingrese la cantidad de filas: "))

for i in range(1, filas + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()