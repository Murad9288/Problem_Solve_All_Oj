for _ in range(int(input())):
    a,b,c = map(int,input().split())
    if a<=b+c and b<=c+a and c<=a+b:
        print("Yes")
    else:
        print("No")
