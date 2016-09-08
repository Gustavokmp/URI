qtd = int(input())
cont = 1
while cont <= qtd:
    lista = input().split()
    lista2= []
    for i in lista:
        if int(i) >= 11 and int(i) <= 20:
            lista2.append(i)
    if len(lista2) %2 != 0:
        lista2.sort()
        tamanho = int((len(lista2)/2))
        print("Case "+str(cont)+":",lista2[tamanho])
    cont +=1
    
