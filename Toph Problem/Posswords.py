try:
    while True:
        s = str(input())
        a=b=c= False
        count = 0
        for i in s:
            if i.islower():
                a = True
            elif i.isupper():
                b = True
            else:
                c = True
            if a and b and c:
                count += 1
                a=b=c=False
        print(count)
except EOFError:
    pass
