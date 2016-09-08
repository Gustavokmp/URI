d = input()
diax = d.split()
linha1 = input()
partes1 = linha1.split(" : ")
d2 = input()
diay = d2.split()
linha2 = input()
partes2 = linha2.split(" : ")
dia1 = int(diax[1])
dia2 = int(diay[1])
h1 = int(partes1[0])
m1 = int(partes1[1])
s1 = int(partes1[2])
h2 = int(partes2[0])
m2 = int(partes2[1])
s2 = int(partes2[2])
if dia1 <= dia2:
    W = (dia2 - dia1)
if h1 < h2 or (h1 - h2) == 0:
    X = (h2 - h1)
if m1 <= m2:
    Y = (m2 - m1)
if s1 <= s2:
    Z = (s2 - s1)
if h1 > h2:
    X = (24-(h1 - h2))
    W = (W -1)
if m1 > m2:
    Y = (60-(m1-m2))
    X = (X - 1)
if s1 > s2:
    Z = (60 -( s1 - s2))
    Y = (Y - 1)
print(W,"dia(s)")
print(X,"hora(s)")
print(Y,"minuto(s)")
print(Z,"segundo(s)")