n, k = map(int, input().strip().split())

luck = 0
li = []

for i in range(n):
    L, T = list(map(int, input().strip().split()))
    if T == 0:
        luck += L
    else:
        li.append(L)

for j in sorted(li, reverse=True):
    if k > 0:
        luck += j
        k -= 1
    else:
        luck -= j

print(luck)
