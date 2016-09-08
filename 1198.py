while True:
    try:
        numeros = input()
        numeros = numeros.split()
        n1 = int(numeros[0])
        n2 = int(numeros[1])
        diferenca = n1 - n2
        if diferenca < 0:
            diferenca *= -1
        print(diferenca)
    except:
        break
