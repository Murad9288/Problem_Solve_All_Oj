for _ in range(int(input())):
    p,q,r = map(int,input().split())
    temp = 1
    for i in range(1,q+1):
        print(i)
        temp *= p
    res = temp%r
    if r<=100:
        print("Result = %d"%res)
    else:
        break
