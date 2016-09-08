while True:
    linha = input().split()
    x1 = int(linha[0])
    y1 = int(linha[1])
    x2 = int(linha[2])
    y2 = int(linha[3])
    if x1+x2+y1+y2 == 0:
        break
    else:
        if(x1 == x2 and y1 == y2):
            print(0)
        elif ((x2-x1) == -(y2-y1) or -(x2-x1) == -(y2-y1) or -(x2-x1) == (y2-y1) or (x2-x1) == (y2-y1)):
            print(1)
        elif (x1 == x2 or y1 == y2):
            print(1)
        else:
            print(2)
