cont = 0
numero = int(input())
while cont < numero:
    lista = input().split()
    n1 = lista[0]
    n2 = lista[1]
    qtd = 1
    for i in range(len(n2)):
        qtd *= 10
    if int(n1)%qtd == int(n2):
        print("encaixa")
    else:
        print("nao encaixa")
    cont += 1
