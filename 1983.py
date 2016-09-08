num = int(input())
cont = 0
maior_nota = 0
matricula_maior_nota = 0
while cont < num:
    lista = input().split()
    matricula = int(lista[0])
    nota = float(lista[1])
    if nota > maior_nota:
        maior_nota = nota
        matricula_maior_nota = matricula
    cont += 1
if maior_nota < 8:
    print("Minimum note not reached")
else:
    print(matricula_maior_nota)
