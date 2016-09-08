num = input().split()
n1 = int(num[0])
n2 = int(num[1])
cont = 1
cont2 = 0
soma = ""
while cont < n2:
    while cont2 < n1:
        soma = soma + str(cont) + " "
        if cont == n2:
            cont2 = n1
        cont += 1
        cont2 += 1
    cont2 = 0
    print(soma[0:-1])
    soma = ""
    
