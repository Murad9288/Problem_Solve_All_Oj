from functools import reduce

def baseconv(n, b):
    newbase = []
    if n < b:
        return 0
    if n == b:
        return [1]
    while True:
        r = n % b
        newbase.insert(0, r)
        n = n // b
        if n == 0:
            break
    return newbase

t = int(input())
for i in range(t):
    n, p = map(int, input().split())
    base = baseconv(n, p)
    nonzeros = reduce(lambda x, y: x * y, (z + 1 for z in base))
    print(n - nonzeros + 1)
