x, y = list(map(int,input().split()))
c = 1
for i in range(1,(y//x)+1):
    res = ""
    for j in range(x):
        res += str(c) + " "
        c += 1
    print(res[:-1])
