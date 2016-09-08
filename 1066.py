cont = 1
par = 0
imp = 0
pos = 0
negat = 0
while cont <= 5:
    a = int(input())
    if (a%2) == 0 :
        par += 1
    if (a%2) == 1:
        imp += 1
    if a < 0:
        negat += 1
    if a > 0:
        pos += 1
    cont += 1
print (par,"valor(es) par(es)")
print (imp,"valor(es) impar(es)")
print (pos,"valor(es) positivo(s)")
print (negat,"valor(es) negativo(s)")
