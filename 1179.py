p = 0
i = 0
par = []
impar = []
cont = 0
while(cont < 15):
    a = int(input())
    if(a%2 == 0):
        par.append(str(a))
        p += 1
    else:
        impar.append(str(a))
        i += 1
    if(p == 5):
        b = 0
        while(b != 5):
            print("par["+str(b)+"] =",par.pop(0))
            b += 1
        p = 0
    if(i == 5):
        b = 0
        while(b != 5):
            print("impar["+str(b)+"] =",impar.pop(0))
            b += 1
        i = 0
    if(cont == 14):
        b = 0
        while(b < i):
            print("impar["+str(b)+"] =",impar.pop(0))
            b += 1
        b = 0
        while(b < p):
            print("par["+str(b)+"] =",par.pop(0))
            b += 1       
    cont += 1
