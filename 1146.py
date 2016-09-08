cont = 0
cont2 = 1
soma = ""
while cont < 1:
    num = int(input())
    if num != 0:
        while cont2 <= num:
            soma = (soma + str(cont2) + " ")
            cont2 += 1
        print(soma[0:-1])
        soma = ""
        cont2 = 1
    else:
        cont += 1
            
