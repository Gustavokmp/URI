a = 0
g = 0
d = 0
cont = 0
while cont < 1:
    p = int(input())
    if p == 1:
        a = a + 1
    if p == 2:
        g = g + 1
    if p == 3:
        d = d + 1
    if p == 4:
        cont += 1
print("MUITO OBRIGADO")
print("Alcool: " + str(a))
print("Gasolina: " + str(g))
print("Diesel: " + str(d))
