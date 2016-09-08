qtd = int(input())
cont = 0
while cont < qtd:
    cont2 = 0
    acumulador = 1
    while cont2 < 1:
        numero = int(input())
        cont3 = 0
        while cont3 < numero:
            acumulador *= 2
            cont3 += 1
        cont2 += 1
    acumulador = int(acumulador/12)
    acumulador = int(acumulador/1000)
    print(acumulador,"kg")
    cont += 1
