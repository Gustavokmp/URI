cont = 0
cont2 = 0
notas = 0
while cont < 1:
    while cont2 < 2:
        x = float(input())
        if 0 <= x <= 10:
            notas = notas + x
            cont2 +=1
        else:
            print("nota invalida")
        if cont2 == 2:
            print("media = %.2f" % (notas/2))
    print("novo calculo (1-sim 2-nao)")
    y = int(input())
    if y == 1:
        cont2 = 0
        notas = 0
    if y == 2:
        cont += 1
