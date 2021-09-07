# First Rules:
# Accepted:

n = int(input())
k = int(input())
arr = []
for i in range(n):
    li = int(input())
    arr.append(li)
arr.sort()
m = arr[-1]
for i in range(len(arr)-k+1):
    mi = arr[i]
    mx = arr[k-1]
    m = min(m,mx-mi)
    k = k+1
print(m)


# Second Rules:
# Accepted:

'''
n = int(input())
k = int(input())
arr = []
for i in range(n):
    li = int(input())
    arr.append(li)
arr.sort()
i = 0
result = arr[k-1] - arr[0]
for i in range(n - k + 1):
    temp = arr[i + k - 1] - arr[i]
    if temp < result:
        result = temp
print(result)
'''
