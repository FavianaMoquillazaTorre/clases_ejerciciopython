nombres =["Ana", "Sonia", "Helena"]
nombres2 =["Miquel", "Carlos", "Juan"]
nombresfinales =[nombres, nombres2]
print("Imprimiendovalor [0][1]", nombresfinales [0][1])
print("Lista completa: ", nombresfinales)

for i in range(len(nombresfinales)):
    print("\n")
    if i == 0:
        print("///// Nombres Femeninos /////")
    elif i == 1:
        print("///// Nombres Masculinos /////")
    for j in range(len(nombresfinales[i])):
        print(nombresfinales [i][j], end=", ")
