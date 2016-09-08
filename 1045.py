lista = input()
numeros = lista.split()
a = float(numeros[0])
b = float(numeros[1])
c = float(numeros[2])
if a <= b :
     menor = a
     a = b
     b = menor
if b <= c:
    menor = b
    b = c
    c = menor
if a <= b:
    menor = a
    a = b
    b = menor
if a >= (b+c):
    print("NAO FORMA TRIANGULO")
else:
    if (a**2) == ((b**2)+(c**2)):
        print("TRIANGULO RETANGULO")
    if (a**2) > ((b**2)+(c**2)):
        print("TRIANGULO OBTUSANGULO")
    if (a**2) < ((b**2)+(c**2)):
        print("TRIANGULO ACUTANGULO")
    if a == b == c:
        print("TRIANGULO EQUILATERO")
    if a == b and c != a or b == c and b != a or a == c and a != b:
        print("TRIANGULO ISOSCELES")