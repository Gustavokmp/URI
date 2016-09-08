def carryadd(n1,n2):
    a = 0
    b = 0
    c = 0
    carry = 0
    while True:
        a = n1%10
        b = n2%10
        n1 =int(n1/10)
        n2 =int(n2/10)
        if (a+b+c) >= 10:
            carry += 1
            c = 1
        else:
            c = 0
        if n1 ==0 and n2 == 0:
            break
    return carry

while True:
    linha = input().split()
    n1 = int(linha[0])
    n2 = int(linha[1])
    if n1 == 0 and n2 == 0:
        break
    carry = carryadd(n1,n2)
    if carry == 0:
        print("No carry operation.")
    elif carry == 1:
        print("1 carry operation.")
    else:
        print(carry,"carry operations.")

            
