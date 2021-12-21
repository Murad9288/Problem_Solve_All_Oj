n = int(input())
sum = 0
count = 0
for i in range(n):
    a,b = map(int,input().split())
    sum += a - b
    if sum < 0:
        sum = 0
        count = i+1
print(count)
