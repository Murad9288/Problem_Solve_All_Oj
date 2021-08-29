for _ in range(int(input())):
    x,y,z = map(int,input().split())
    if x%z == 0:
        for i in range(x,y+1,z):
            print(i)
    else:
        for j in range(x,y+1):
            if j%z == 0:
                print(j)
    print()
