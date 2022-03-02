for t in range(int(input())):
    n = int(input())
    fail = 0
    s = 0
    c2 = 0
    for _ in range(n):
        st = input().split()
        m = float(st[0])
        c = float(st[1])
        if m>=80.0 and m<=100.0:
            s += 4.00*c
            c2 += c
        elif m>=75.0 and m<=79.9:
            s += 3.75*c
            c2 += c
        elif m>=70.0 and m<=74.9:
            s += 3.50*c
            c2 += c
        elif m>=65.0 and m<=69.9:
            s += 3.25*c
            c2 += c
        elif m>=60.0 and m<=64.9:
            s += 3.00*c
            c2 += c
        elif m>=55.0 and m<=59.9:
            s += 2.75*c
            c2 += c
        elif m>=50.0 and m<=54.9:
            s += 2.50*c
            c2 += c
        elif m>=45.0 and m<=49.9:
            s += 2.25*c
            c2 += c
        elif m>=40.0 and m<=44.9:
            s += 2.00*c
            c2 += c
        else:
            fail += 1
    if fail == 1:
        print("Case %d: Sorry, you have failed in 1 course!"%(t+1))
    elif fail == 0:
        print("Case %d: %.2f"%(t+1,s/c2))
    else:
        print("Case %d: Sorry, you have failed in %d courses!"%(t+1,fail))
