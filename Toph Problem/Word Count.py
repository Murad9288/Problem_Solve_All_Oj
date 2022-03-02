def count(a):
    if a[-1] == '.':
        a = a[0:len(a) - 1]
    if a in d:
        d[a] += 1
    else:
        d.update({a: 1})
lst = []
while True:
    try:
        s = list(map(str,input().split()))
        for i in s:
            lst.append(i)
    except EOFError:
        break       
d = {}
for e in lst:
    count(e)
res = max(zip(d.values(), d.keys()))[1]
print(res)
