N = int(input())
li = list(map(int,input().split()))
r = sorted(li)
if li == r :
    print("Yes")
else:
    print("No")
