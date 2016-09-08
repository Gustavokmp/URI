lista = input()
numeros = lista.split()
a = int(numeros[0])
b = int(numeros[1])
c = int(numeros[2])
d = int(numeros[3])
if a > c:
    hora = (24-(a - c))
if a < c:
     hora = (c - a)
if b < d:
    minuto = (d - b)
if b > d:
    minuto = (60 - (b - d))
    menos = (hora - 1)
    hora = menos
if a == c and b == d:
    hora = 24
    minuto = 0
print("O JOGO DUROU",hora,"HORA(S) E",minuto,"MINUTO(S)")
