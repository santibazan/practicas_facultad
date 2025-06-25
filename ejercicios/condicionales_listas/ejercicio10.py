# Mostrar solo vocales de una palabra
# Recorrer una palabra letra por letra e imprimir solo si es vocal
palabra="universidad"
for i in range(len(palabra)):
    if palabra[i] == "a" or palabra[i] == "e" or palabra[i] == "i" or palabra[i] == "o" or palabra[i] == "u":
        print(f"La letra {palabra[i]} es vocal")