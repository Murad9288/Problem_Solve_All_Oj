for _ in range(int(input())):
    a,b = map(int,input().split())
    if b>a:
        for i in range(a,b+1,a):
            print(i)
    else:
        print("Invalid!")
    print()
