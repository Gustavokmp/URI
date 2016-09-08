cont = 0
qtd = int(input())
while cont < qtd:
    linha = input().split()
    string1 = linha[0]
    string2 = linha[1]
    acumulador = ""
    cont2 = 0
    while cont2 < len(string1) and cont2 < len(string2):
        acumulador += string1[cont2] + string2[cont2]
        cont2 += 1
    if cont2 < len(string1):
        acumulador+= string1[cont2:]
    if cont2 < len(string2):
        acumulador += string2[cont2:]
    print(acumulador)
    cont += 1
