# 1st system:

m = None
h = []
for _ in range(int(input())):
    arr = list(map(int,input().split()))
    if arr[0] == 1:
        h.append(arr[1])

        if m == None:
            m = arr[1]

        elif arr[1] < m:
            m = arr[1]

    elif arr[0] == 2:
        h.remove(arr[1])

        if arr[1] == m and len(h) != 0:
            m = min(h)
        elif arr[1] == m and len(h) == 0:
            m = None
    else:
        print(m)
        
# Second System:
'''
import heapq
s = set()
h = []
for _ in range(int(input())):
    arr = list(map(int, input().split()))
    if arr[0] == 1:
        heapq.heappush(h, arr[1])
    if arr[0] == 2:
        s.add(arr[1])
    if arr[0] == 3:
        while True:
            r = heapq.heappop(h)
            if r not in s:
                print(r)
                heapq.heappush(h, r)
                break
                
'''
