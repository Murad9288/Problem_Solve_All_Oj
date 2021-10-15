# 1st System.

n = int(input())
arr = list(map(int, input().split()))
z = max(arr)
while max(arr) == z:
    arr.remove(max(arr))
print(max(arr))

# Second System.
'''
n = int(input())
arr = list(map(int, input().split()))
zes = max(arr)
i=0
while(i<n):
    if zes ==max(arr):
        arr.remove(max(arr))
    i+=1
print(max(arr))

'''
