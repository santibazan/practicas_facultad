# Buscar un número en una lista
# Pedir un número y verificar si está en una lista. Usar break si se encuentra

listaNum = [1,3,7,10,12,15,20]

numABuscar = int(input("Ingrese un numero a buscar en la lista: "))
encontrado = False

for i in range(len(listaNum)):
    if listaNum[i] == numABuscar:
        print(f"El numero {numABuscar} se encuentra en la lista")
        encontrado = True
        break

if not encontrado:
    print(f"El número {numABuscar} NO se encuentra en la lista")