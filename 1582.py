def mdc(num1,num2):
    resto = None
    while resto is not 0:
        resto = num1%num2
        num1 = num2
        num2 = resto
    return num1

def pitagoras(a,b,c):
    hip = 0
    sum_all = 0
    hip = max(a,(max(b,c)))
    sum_all = pow(a,2) + pow(b,2) + pow(c,2)
    if pow(hip,2) == sum_all - pow(hip,2):
        if mdc(a,mdc(b,c)) == 1:
            return ("tripla pitagorica primitiva")
        else:
            return ("tripla pitagorica")
    if(pow(hip,2) == sum_all - pow(hip,2)) == False:
        return ("tripla")
while True:
    try:
        num = input()
        num = num.split()
        a = int(num[0])
        b = int(num[1])
        c = int(num[2])
        print(pitagoras(a,b,c))
    except:
        break
