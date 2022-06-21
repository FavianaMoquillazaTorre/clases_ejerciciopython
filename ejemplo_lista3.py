paises = []
for x in range(5):
    nombre = input("Ingresar el nombre del pais: ")
    paises.append(nombre)
for k in range(4):
    for x in range(4):
        if paises[x] > paises[x + 1]:
            aux = paises[x]
            paises[x] = paises[x + 1]
            paises[x + 1] = aux
print("Listas de paises: ")
print(paises)