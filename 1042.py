lista = input()
numero = lista.split()
a = int(numero[0])
b = int(numero[1])
c = int(numero[2])
if a > b and b > c:
    print(c)
    print(b)
    print(a)
elif a > c and c > b :
    print(b)
    print(c)
    print(a)
elif b > a and a > c:
    print(c)
    print(a)
    print(b)
elif b > c and c > a:
    print(a)
    print(c)
    print(b)
elif c > a and a > b:
    print(b)
    print(a)
    print(c)
elif c > a and b > a:
    print(a)
    print(b)
    print(c)
print()
print (a)
print (b)
print (c)