while True:
    try:
        numero = input()
        numero = numero.split()
        n1 = int(numero[0])
        n2 = int(numero[1])
        soma_total = 0
        soma_n1 = 0
        soma_n2 = 0
        if(n1 == 0):
            soma_total += 1
        if(n2 == 0):
            soma_total += 1
        if(n1 != 0):
            soma_n1 = 1
            for i in range(2,(n1+1)):
                soma_n1 *= i
        if(n2 != 0):
            soma_n2 = 1
            for i in range(2,(n2+1)):
                soma_n2 *= i
        soma_total += soma_n1 + soma_n2
        print(soma_total)
    except:
        break
