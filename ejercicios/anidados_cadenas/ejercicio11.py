# Mostrar todas las combinaciones de dos listas
# Ej.: colores = ["rojo", "azul"], talles = ["S", "M"]
# Resultado: rojo-S, rojo-M, azul-S, azul-M

colores = ["rojo", "azul", "amarillo", "naranja"]
talles = ["XS", "S", "M", "L","XL"]

for i in range (len(colores)):
    for x in range (len(talles)):
        print(f"{colores[i]}-{talles[x]}")