for _ in range(int(input())):
    a,b,p,q = map(int,input().split())
    if abs(a-p) == abs(b-q):
        print("Yes")
    else:
        print("No")
