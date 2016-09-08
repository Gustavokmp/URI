matriz = []
linha = []
l = 0
c = int(input())
op = input()
cont = 0
cont2 = 0
soma = 0
soma2 = 0
lista = []
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
    while l < 12:  
        soma = matriz[l]
        soma2 = soma[c]
        lista.append(soma2)
        l += 1
    print(sum(lista))
if op == "M":
    while l < 12:  
        soma = matriz[l]
        soma2 = soma[c]
        lista.append(soma2)
        l += 1
    print("%.1f" %(sum(lista)/12))