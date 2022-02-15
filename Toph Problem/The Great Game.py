for t in range(int(input())):
    s = str(input())
    sum = 0
    for i in s:
        sum += int(i)
    if len(s)%2 == 0 and sum%2 == 0 or len(s)%2 == 1 and sum%2 == 1:
        print("Case %d: Safe to push" % (t + 1))
    else:
        print("Case %d: BOOM" % (t + 1))
