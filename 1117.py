cont = 0
notas = 0
while cont < 2:
    nota = float(input())
    if 0 <= nota <= 10:
        notas = notas + nota
        cont += 1
    else:
        print("nota invalida")
print("media = %.2f" % (notas/2))
        
