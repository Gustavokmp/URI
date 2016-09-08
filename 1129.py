def leitura(array):
    cont = 0
    saida = ""
    if array[0] <= 127:
        saida = "A"
        cont += 1
    
    if array[1] <= 127:
        saida = "B"
        cont += 1
    
    if array[2] <= 127:
        saida = "C"
        cont += 1
    
    if array[3] <= 127:
        saida = "D"
        cont += 1
    
    if array[4] <= 127:
        saida = "E"
        cont += 1

    if cont > 1 or cont == 0:
        saida = "*"

    return saida

while(True):
    n = int(input())
    if n == 0: break
    for i in range(n):
        lista = list(map(int, input().split()))
        print(leitura(lista))
