n = int(input())
arr = list(map(int,input().split()))[:n]
c = 0
for i in range(len(arr)):
    if arr[i]%7 == 0:
        c += 1
if c == 13:
    print("Luckily Unlucky")
else:
    print("Lucky")
