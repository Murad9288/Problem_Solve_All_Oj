#Accepted:
#simple input():
'''
6 7
1 2 3 9 10 12
'''
#simple output:
'''
2
'''


from heapq import heapify , heappop , heappush

n, k = map(int,input().split())
my_heap = list(map(int,input().split()))
heapify(my_heap)

count = 0
while my_heap[0] < k :
    a=heappop(my_heap)
    if len(my_heap) == 0:
        print(-1)
        exit()
    b = heappop(my_heap)
    heappush(my_heap, a+2*b)
    count += 1
        

print(count)
