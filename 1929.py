lista = input().split()
n1 = int(lista[0])
n2 = int(lista[1])
n3 = int(lista[2])
n4 = int(lista[3])

if n1 < n2+n3 and n2 < n1+n3 and n3 < n1+n2:
    print("S")
elif n1 < n3+n4 and n3 < n1+n4 and n4 < n1+n3:
    print("S")
elif n1 < n2+n4 and n2 < n1+n4 and n4 < n1+n2:
    print("S")
elif n2 < n3+n4 and n3 < n2+n4 and n4 < n2 +n3:
    print("S")
else:
    print("N")
