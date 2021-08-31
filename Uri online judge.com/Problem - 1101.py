# First Rules:

while True:
    a,b = map(int,input().split())
    sum = 0
    li = []
    if a<=b:
        if a>0 and b>0:
            for i in range(a,b+1):
                li.append(i)
                sum += i
        else:
            break
    else:
        if a>0 and b>0:
            for j in range(b,a+1):
                li.append(j)
                sum += j
        else:
            break
    print(*li,"Sum=%d"%(sum))


# Second Rules:
'''
while True:
    M,N = map(int,input().split())
    if M<=0 or N<=0:
        break
    sum = 0
    if M>=N:
        for i in range(N,M+1):
            sum += i
            print(i,end=" ")
        print("Sum=%d"%sum)
    else:
        for i in range(M,N+1):
            sum += i
            print(i,end=" ")
        print("Sum=%d"%sum)
'''
