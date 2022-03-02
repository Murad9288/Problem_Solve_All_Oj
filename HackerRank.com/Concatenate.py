import numpy as np
N, M, P = map(int, input().split())
arr = []
for _ in range(N+M):
    arr.append(list(map(int,input().split())))
print(np.array(arr))
