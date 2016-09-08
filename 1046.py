lista = input()
tempo = lista.split()
a = int(tempo[0])
b = int(tempo[1])
if a > b:
    duracao = (24 - (a - b))
    print("O JOGO DUROU",duracao,"HORA(S)")
if a < b:
    duracao = (b - a)
    print("O JOGO DUROU",duracao,"HORA(S)")
if a == b:
    print("O JOGO DUROU 24 HORA(S)")
