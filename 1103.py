while True:
    linha = input().split()
    h1 = int(linha[0])
    m1 = int(linha[1])
    h2 = int(linha[2])
    m2 = int(linha[3])
    inicio = 0
    fim = 0
    if m1+m2+h1+h2 == 0:
        break
    if h1 == 0:
        inicio = (24*60)+m1
    else:
        inicio = (h1*60) + m1
    if h2 == 0:
        fim =(24*60)+m2
    else:
        fim = (h2*60) + m2
    if fim > inicio:
        print(fim-inicio)
    else:
        print((24*60)-(inicio-fim))
