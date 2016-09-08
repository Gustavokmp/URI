
while True:
    try:
        linha = input()
        linha = linha.split()
        r1 = int(linha[0])
        x1 = int(linha[1])
        y1 = int(linha[2])
        r2 = int(linha[3])
        x2 = int(linha[4])
        y2 = int(linha[5])
        distancia = (((x2-x1)**2)+((y2-y1)**2))**0.5
        if r1 >= distancia+r2:
            print("RICO")
        else:
            print("MORTO")
    except:
        break
