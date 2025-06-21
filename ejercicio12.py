# Contar cuántas veces aparece una letra en una frase
# Pedir una letra y contar cuántas veces aparece en un string dado

frase="Haciendo las practicas para la facultad"
letra=input("Ingrese una letra para verificar si se encuentra en la frase: ")
suma = 0
for i in range(len(frase)):
    if frase[i].lower() == letra.lower():
        suma += 1

if suma == 1:
    print(f"La letra '{letra}' aparece 1 vez")
else:
    print(f"La letra '{letra}' aparece {suma} veces")