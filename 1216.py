cont = 0
distancia = 0
while True:
    try:
        lista = input()
        num = int(input())
        distancia += num
        cont += 1
        
    except:
        print("%.1f" % (distancia/cont))
        break
