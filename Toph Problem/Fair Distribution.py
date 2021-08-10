x,y = map(int,input().split())
if x<y:
    temp = y
    while x<=y:
        if y%x == 0:
            break
        else:
            y += 1
    print(y-temp)
else:
    print(x-y)
