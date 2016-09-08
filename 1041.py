valores = input()
lista = valores.split()
x = float(lista[0])
y = float(lista[1])
if x > 0 and y > 0:
    print("Q1")
elif x < 0 and y > 0:
    print("Q2")
elif x < 0 and y < 0:
    print("Q3")
elif x > 0 and y < 0:
    print("Q4")
elif x == 0 and y != 0:
    print("Eixo Y")
elif x != 0 and y == 0:
    print("Eixo X")
else:
    print("Origem")
