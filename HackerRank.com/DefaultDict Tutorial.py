from collections import defaultdict
n , m = map(int,input().split())

A = [input() for i in range(n)]
B = [input() for i in range(m)]

d = defaultdict(list)
for i in range(len(A)):
    d[A[i]].append(str(i+1))
for i in B:
    if i in A:
        print(' '.join(d[i]))
    else:
        print(-1)
