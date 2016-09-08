qtd = int(input())
cont = 0
while cont < qtd:
    lista = input().split()
    qtd_alunos = int(lista.pop(0))
    soma = 0
    for i in lista:
        soma += int(i)
    media = int(soma/qtd_alunos)
    acima_da_media = []
    for i in lista:
        if int(i) > media:
            acima_da_media.append(i)
    print("%.3f" %((len(acima_da_media)*100)/qtd_alunos)+"%")
    cont += 1
