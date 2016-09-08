cont = 0
lista = []
while cont < 20:
    x = input()
    lista.append(x)
    cont += 1
cont2 = 0
valor = -1
while cont2 < 20:
    print("N[" + str(cont2) + "] = " + str(lista[valor]))
    valor -= 1
    cont2 += 1
    
