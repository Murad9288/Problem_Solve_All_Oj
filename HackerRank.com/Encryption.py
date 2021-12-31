import math
s = str(input())
n = 0
st = math.ceil(math.sqrt(len(s)))
res = ""
for i in range(n, st, 1):
    res += s[n::st]+" "
    n += 1
print(res)
