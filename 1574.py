qtd = int(input())
cont = 0
while cont < qtd:
    num = int(input())
    lista = []
    cont2 = 0
    p = 0
    
    while cont2 < num:
        istrucao = input()
        if istrucao[0] == "S":
            num2 = int(istrucao[8:])-1
            istrucao = lista[num2]
            
        if istrucao == "LEFT":
            p -= 1
            lista.append(istrucao)
            
        if istrucao == "RIGHT":
            p += 1
            lista.append(istrucao)
        
        cont2 += 1
    print(p)
    
    cont += 1