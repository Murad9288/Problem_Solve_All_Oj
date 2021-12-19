while True:
    n = int(input())
    x = (n-1)%6
    y = (n+1)%6
    if n<=1:
        print("Not Prime")
    elif x == 0 or  y == 0:
        print("Prime")
    elif n == 2 or n == 3:
        print("Prime")
    else:
        print("Not Prime")
