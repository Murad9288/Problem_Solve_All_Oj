for k in range(int(input())):
    n = int(input())
    if n <= 10:
        f = 1
        j = -4
        for i in range(1,n+1):
            f *= i
        F = f
        result = list(map(int,str(F)))
        if len(result) < 4:
           print("Case %d: %d"%(k+1,F))
        else:
            while True:
                print(result[j],end='')
                j += 1
                if j == 0:
                    break
    else:
        print("Case %d: %d"%(k+1,0))
