for _ in range(int(input())):
    a,b,c = list(map(int,input().split()))
    if a+b>=c and b+c>=a and c+a>=b:
        s = (a+b+c)/2
        area = (s * (s-a) * (s-b) * (s-c))**0.5
        print("%0.2f"%area)
    else:
        print("Oh, No!")
