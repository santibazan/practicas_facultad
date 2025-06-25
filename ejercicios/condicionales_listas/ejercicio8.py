# Contar cuántos números mayores a 10 hay en una lista
# Recorrer una lista de números y contar cuántos son mayores a 10

listaNum = [1,3,7,10,12,15,20]

for i in range(len(listaNum)):
    if listaNum[i]>10:
        print(listaNum[i])
