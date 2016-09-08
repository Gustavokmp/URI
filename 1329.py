while True:
    qtd = int(input())
    if qtd == 0:
        break
    jogadas = input().split()
    maria = 0
    joao = 0
    for i in range(qtd):
        if int(jogadas[i]) == 0:
            maria += 1
        else:
            joao += 1
    print("Mary won "+str(maria)+" times and John won "+str(joao)+" times")
