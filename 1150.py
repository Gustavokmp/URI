x = int(input())
z = int(input())
cont = 0
while cont < 1:
    if z <= x:
        z = int(input())
    else:
        cont += 1
soma = 0
cont2 = 0
cont3 = 0
while cont2 < 1:
    soma = soma + x
    if soma > z:
        cont2 += 1
    cont3 += 1
    x += 1
print(cont3)
