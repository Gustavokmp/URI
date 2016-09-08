i = 0
while i < 1.8:
    j = 0
    j2 = 0
    while j < 3:
        j+= 1
        j2 = i+j
        if j2 % 1== 0 and i % 1 == 0:
            print("I=%d J=%d" %(i,j2))
        else:
            print("I=%.1f J=%.1f" % (i,j2))
    i += 0.2
print("I=2 J=3\nI=2 J=4\nI=2 J=5")
