continua = True
while continua:
    linha = input().split()
    n1 = int(linha[0])
    n2 = int(linha[1])
    if n1 == 0 and n2 == 0:
        continua = False
    else:
        print(n1+n2)
