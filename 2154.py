def derivada(polinomo):
    pos_x = polinomo.find("x")
    n1 =int( polinomo[:pos_x])
    n2 = int(polinomo[(pos_x+1):])
    n1 *= n2
    if (n2-1) < 2:
        n2 = ""
    else:
        n2 -= 1
    novo = str(n1)+"x"+str(n2)
    return novo



while True:
    try:
        qtd = int(input())
        p = input()
        p = p.split()
        pronto = ""
        cont = 0
        achadas = 0
        while True:
            if achadas == qtd:
                break
            if len(p[cont]) == 1:
                pronto += " + "
            else:
                achadas += 1
                pronto += str(derivada(p[cont]))
            cont += 1
        print(pronto)
    except:
        break
