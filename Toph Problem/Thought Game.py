for _ in range(int(input())):
    a,b = map(int,input().split())
    avg = (a+b)//2
    if avg%2 == 0:
        print("Sadia will be happy.")
    else:
        print("Oops!")
