matriz = []
linha = []
l = int(input())
op = input()
cont = 0
cont2 = 0
while cont < 12:
    while cont2 < 12:
        n = float(input())
        linha.append(n)
        cont2 += 1
    matriz.append(linha)
    cont2 = 0
    linha = []
    cont += 1
if op == "S":
    print(sum(matriz[l]))
if op == "M":
    print("%.1f" %(sum(matriz[l])/12))
