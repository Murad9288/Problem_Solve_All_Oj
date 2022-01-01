# First system:

arr = []
for _ in range(int(input())):
    arr.append(list(map(int,input().split())))
s = 0
c = 0
l = len(arr)-1
for i in range(len(arr)):
    s += arr[i][i]
    c += arr[i][l]
    l -= 1
print(abs(s-c))

# Second System:

"""
arr = []
for _ in range(int(input())):
    arr.append(list(map(int,input().split())))
list1 = []
list2 = []
for i in range(len(arr)):
    list1.append(arr[i][i])
    list2.append(arr[i][-i-1])
print(abs(sum(list1)-sum(list2)))
"""
