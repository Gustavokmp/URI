qtd = int(input())
cont = 0
while cont < qtd:
    erro = 0
    verifica = "one"
    texto = input()
    if len(texto) == 5:
        print(3)
    else:
        for i in range(len(texto)):
            if texto[i] != verifica[i]:
                erro += 1
        if erro > 1:
            print(2)
        else:
            print(1)
    cont += 1
