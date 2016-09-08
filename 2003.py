while True:
    try:
        linha = input()
        linha = linha.split(":")
        h = int(linha[0])
        m = int(linha[1])
        total = (h*60)+m+60
        if total <= 480:
            print("Atraso maximo: 0")
        else:
            print("Atraso maximo:",total-480)
    except:
        break
