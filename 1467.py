while True:
    try:
        linha = input().split()
        a = int(linha[0])
        b = int(linha[1])
        c = int(linha[2])

        if a != b and a != c:
            print("A")
        elif b != a and b!= c:
            print("B")
        elif c != a and c != b:
            print("C")
        else:
            print("*")
    except:
        break
