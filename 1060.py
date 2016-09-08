a = input ()
b = input ()
c = input ()
d = input ()
e = input ()
f = input ()
g = 0
if a == int:
    a = int(a)
    if a >= 0:
        g = g+1
else:
    a = float(a)
    if a >= 0:
        g = g + 1
if b == int:
    b = int(b)
    if a >= 0:
        g = g+1
else:
    b = float(b)
    if b >= 0:
        g = g + 1
if c == int:
    c = int(c)
    if c >= 0:
        g = g+1
else:
    c = float(c)
    if c >= 0:
        g = g + 1
if d == int:
    d = int(d)
    if d >= 0:
        g = g+1
else:
    d = float(d)
    if d >= 0:
        g = g + 1
if e == int:
    e = int(e)
    if e >= 0:
        g = g+1
else:
    e = float(e)
    if e >= 0:
        g = g + 1
if f == int:
    f= int(f)
    if f >= 0:
        g = g+1
else:
    f = float(f)
    if f >= 0:
        g = g + 1
print(g,"valores positivos")