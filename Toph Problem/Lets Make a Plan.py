for _ in range(int(input())):
    a,b,c,d = map(str,input().split())
    if b == c  or a == d or a == c or b == d:
        print("Possible")
    else:
        print("Oh no!, such a shame")
