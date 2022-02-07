import heapq
def cookies(k, arr):
    heapq.heapify(arr)
    ops = 0
    while True:
        f = heapq.heappop(arr)
                
        if f >= k:
            return ops
        
        if len(arr) == 0:
            return -1
        
        s = heapq.heappop(arr)
        n = f + 2*s
        heapq.heappush(arr, n)
        
        ops += 1

if __name__ == '__main__':
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))[:n]
    print(cookies(k, arr))
