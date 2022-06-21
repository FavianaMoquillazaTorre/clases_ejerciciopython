lista = [10, 20, 10, 30, 40, 30, 50, 20, 60, 70]
print("Lista: ")
print(lista)
numlista = []
for element in lista:
    if element not in numlista:
        numlista.append(element)
print("/////////////////////////////////////////")
print("Lista con numeros sin repeticion: ")
print(numlista)