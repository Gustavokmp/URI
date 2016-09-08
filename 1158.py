cont = 0
quant = int(input())
while cont < quant:
    num = input().split()
    x = int(num[0])
    y = int(num[1])
    cont2 = 0
    lista = []
    if x % 2 == 0:
        x += 1
    while cont2 < y:
        lista.append(x)
        cont2 += 1
        x += 2
    print(sum(lista))
    cont += 1
