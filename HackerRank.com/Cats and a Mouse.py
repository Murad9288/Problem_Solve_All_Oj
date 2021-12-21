for _ in range(int(input())):
    a,b,c = map(int,input().split())
    if a > c and b > c:
        a1 = a - c
        b1 = b - c
        if a1 < b1:
            print("Cat A")
        elif a1 > b1:
            print("Cat B")
        else:
            print("Mouse C")
    elif a > c and b < c:
        a2 = a - c
        b2 = c - b
        if a2 < b2:
            print("Cat A")
        elif a2 > b2:
            print("Cat B")
        else:
            print("Mouse C")
    elif a < c and b > c:
        a3 = c - a
        b3 = b - c
        if a3 < b3:
            print("Cat A")
        elif a3 > b3:
            print("Cat B")
        else:
            print("Mouse C")
    else:
        a4 = c - a
        b4 = c - b
        if a4 < b4:
            print("Cat A")
        elif a4 > b4:
            print("Cat B")
        else:
            print("Mouse C")
