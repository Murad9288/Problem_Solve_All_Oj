for _ in range(int(input())):
    a,m = map(int,input().split())
    if a == 0 or pow(a,(m-1)//2,m) == 1:
        print("YES")
    else:
        print("NO")
