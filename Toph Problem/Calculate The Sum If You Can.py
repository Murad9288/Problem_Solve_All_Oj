for _ in range(int(input())):
    n = int(input())
    if n & 1:
        if n == 1:
            print(1)
        elif n == 3:
            print(0)
        else:
            print(-((n-3)//2))
    else:
        print(-(n//2))
