from math import factorial
for T in range(int(input())):

    string = list(map(str, input().split()))
    l = len(string)

    d = {}
    for j in string:
        d[j] = string.count(j)

    count = 1
    for k in d.keys():
        if d[k] > 1:
            count *= factorial(d[k])
    if count == 0:
        count = 1
    print("1/{0}".format(factorial(l)//count))
