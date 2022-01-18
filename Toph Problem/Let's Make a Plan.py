for _ in range(int(input())):
    a,b,c,d = map(str,input().split())
    if a == c or b == d or b == c:
        print("Possible")
    else:
        print("Oh no!, such a shame")
