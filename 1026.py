while True:
    try:
        num = input()
        num = num.split()
        a = int(num[0])
        b = int(num[1])
        print(a^b)
    except:
        break
