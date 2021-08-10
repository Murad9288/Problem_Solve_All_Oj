import  math
for _ in range(int(input())):
    Xc, Yc = list(map(int, input().split()))
    r = int(input())
    X, Y = list(map(int, input().split()))

    s = math.sqrt(((X-Xc)**2) + ((Y-Yc)**2))
    if r > s:
        print("The point is inside the circle")

    else:
        print("The point is not inside the circle")
