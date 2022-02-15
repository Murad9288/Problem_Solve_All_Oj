from itertools import permutations
def cs(t):
    str ="".join(t)
    return str
a,b = input().split()
t = int(b)
arr = list(permutations(a,t))
arr.sort()
for i in range(len(arr)):
    arr[i]=cs(arr[i])
    print(arr[i])
