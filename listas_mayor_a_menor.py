sueldos = []
for x in range(5):
    valor = int(input("Ingresar sueldo: "))
    sueldos.append(valor)
print("Listas sin ordenar: ")
print(sueldos)
for x in range(4):
    if sueldos[x] > sueldos[x + 1]:
        aux = sueldos[x]
        sueldos[x] = sueldos[x + 1]
        sueldos[x + 1] = aux
print("Listas con el ultimo elemento ordenado: ")
print(sueldos)