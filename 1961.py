lista = input().split()
lista2 = input().split()
pulo = int(lista[0])
quant_canos = int(lista[1])
cont = 0
resposta = True
while cont < quant_canos:
    if cont < (quant_canos-1):
        a = int(lista2[cont])
        b = int(lista2[cont+1])
        soma = a-b
        if soma < 0:
            soma *= -1
        if soma > pulo:
            resposta = False
    cont += 1
if resposta:
    print("YOU WIN")
else:
    print("GAME OVER")
    
