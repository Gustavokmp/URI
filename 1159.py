cont = 0
while (cont < 1):
    numero = int(input())
    if(numero == 0):
        cont +=1
    else:
        if(numero%2 != 0):
            numero += 1
        cont2 = 1
        soma = 0
        while(cont2 <= 5):
            soma += numero
            numero += 2
            cont2 += 1
        print(soma)
            