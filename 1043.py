lista = input()
numeros = lista.split()
a = float(numeros[0])
b = float(numeros[1])
c = float(numeros[2])
if (a+b) > c and (b+c) > a and (a+c) > b:
    calculo = (a+b+c)
    print("Perimetro = %.1f" % calculo)
else:
    calculo2 = (((a+b)*c)/2)
    print("Area = %.1f" % calculo2)
