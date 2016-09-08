cont = 0
while cont < 1:
    num = int(input())
    if num != 0:
        print(int((num*(num+1)*((2*num)+1))/6))
    else:
        cont += 1
    
