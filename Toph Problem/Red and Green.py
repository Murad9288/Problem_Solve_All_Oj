for _ in range(int(input())):
    n,m = map(int,input().split())
    for _ in range(m):
        x,y = map(int,input().split())
        if x == y:
            if x%2 != 0:
                print(1,0)
            else:
                print(0,1)
        elif x%2 != 0 and y%2 == 0:
            print(((y-x)//2)+1,((y-x)//2)+1)
        elif x%2 == 0 and y%2 != 0:
            print(((y-x)//2)+1,((y-x)//2)+1)
        elif x%2 != 0 and y%2 != 0:
            print(((y-x)//2)+1,(y-x)//2)
        elif x%2 == 0 and y%2 == 0:
            print(((y-x)//2),((y-x)//2)+1)
