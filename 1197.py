while True:
    try:
        numeros = input()
        numeros = numeros.split()
        n1 = int(numeros[0])
        n2 = int(numeros[1])
        print(n1*n2*2)
    except:
        break
