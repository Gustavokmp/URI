cont = 1
while True:
    try:
        condicao = int(input())
        linha = input()
        linha = linha.split()
        if cont != 1:
            print()
        f = 0
        m = 0
        for i in range(0,len(linha),2):
            if int(linha[i]) == condicao:
                if linha[i+1] == "F":
                    f += 1
                else:
                    m += 1
        print("Caso "+str(cont)+":")
        print("Pares Iguais:", (m+f))
        print("F:",f)
        print("M: "+str(m))
        cont += 1
            
    except:
        break
