#Accepted:
from sys import stdin
s = ""
for c in stdin:
    s += (c+' ')
lst = list(map(int, s.split()))
test = lst[0]
del lst[0]
for t in range(test):
    n = lst[0]
    del lst[0]
    flist = list()
    for i in range(n):
        flist.append(lst[0])
        del lst[0]
    m = lst[0]
    del lst[0]
    for i in range(m):
        flist.append(lst[0])
        del lst[0]
    flist.sort()
    for i in range(len(flist)):
        if i > 0:
            print("",end=" ")
        print(flist[i],end="")
    print()

#Second Rules:
#Not Ac:
# Runtime Error:

for T in range(int(input())):
    n1 = int(input())
    a = list(map(int, input().split()))
    n2 = int(input())
    b = list(map(int, input().split()))
    arr = sorted(a + b)
    for i in range(0, len(arr)):
        if (i < len(arr) - 1): # if(i != len(arr)-1:
            print(arr[i], end=' ')
        else:
            print(arr[i]
