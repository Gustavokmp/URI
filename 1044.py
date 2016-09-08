lista = input()
numeros = lista.split()
a = int(numeros[0])
b = int(numeros[1])
if (a%b) == 0 or (b%a) == 0:
    print ("Sao Multiplos")
else:
    print ("Nao sao Multiplos")
