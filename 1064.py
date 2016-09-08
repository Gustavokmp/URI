a = input ()
b = input ()
c = input ()
d = input ()
e = input ()
f = input ()
g = 0
nota1 = 0
nota2 = 0
nota3 = 0
nota4 = 0
nota5 = 0
nota6 = 0

if a == int:
    a = int(a)
    if a >= 0:
        g = g+1
        nota1 = a
else:
    a = float(a)
    if a >= 0:
        g = g + 1
        nota1 = a
if b == int:
    b = int(b)
    if a >= 0:
        g = g+1
        nota2 = b
else:
    b = float(b)
    if b >= 0:
        g = g + 1
        nota2 = b
if c == int:
    c = int(c)
    if c >= 0:
        g = g+1
        nota3 = c
else:
    c = float(c)
    if c >= 0:
        g = g + 1
        nota3 = c
if d == int:
    d = int(d)
    if d >= 0:
        g = g+1
        nota4 = d
else:
    d = float(d)
    if d >= 0:
        g = g + 1
        nota4 = d
if e == int:
    e = int(e)
    if e >= 0:
        g = g+1
        nota5 = e
else:
    e = float(e)
    if e >= 0:
        g = g + 1
        nota5 = e
if f == int:
    f= int(f)
    if f >= 0:
        g = g+1
        nota6 = f
else:
    f = float(f)
    if f >= 0:
        g = g + 1
        nota6 = f
print(g,"valores positivos")
print((nota1+nota2+nota3+nota4+nota5+nota6)/g)
