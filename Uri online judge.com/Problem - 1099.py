for _ in range(int(input())):
    x,y = map(int,input().split())
    sum = 0
    if x>=y:
        if y%2==0:
            for i in range(y+1,x,2):
                sum += i
        else:
            for i in range(y+2,x,2):
                sum += i
    else:
        if x%2==0:
            for i in range(x+1,y,2):
                sum += i
        else:
            for i in range(x+2,y,2):
                sum += i
    print(sum)
