num = int(input())
cont = 1
soma = 0
cont2 = 0
while cont2 < num:
    n1 = int(input())
    while cont<n1:
        if n1%cont==0:
            soma = soma + cont
            cont = cont + 1
        else:
            cont = cont + 1     
    if soma==n1:
        print(n1,"eh perfeito")
    else:
        print(n1,"nao eh perfeito")
    cont2 += 1
    soma = 0
    cont = 1
