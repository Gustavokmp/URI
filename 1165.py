cont = 0
rep = int(input())
div = 1
primo = 0
while cont < rep:
    num = int(input())
    while div <= num:
        if num % div == 0:
            primo = primo + 1
        div += 1
    if primo == 2:
        print(num,"eh primo")
    else:
        print(num,"nao eh primo")
    cont += 1
    div = 1
    primo = 0
