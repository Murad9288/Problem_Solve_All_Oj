for t in range(int(input())):
    a,b,c = map(int,input().split())
    li = [a,b,c]
    m = max(li)
    count = 0
    for i in li:
        if m == i:
            count += 1
    if count == 1 and m == a:
        print("Case %d: A"%(t+1))
    elif count == 1 and m == b:
        print("Case %d: B"%(t+1))
    elif count == 1 and m == c:
        print("Case %d: C"%(t+1))
    else:
        print("Case %d: Confused"%(t+1))
