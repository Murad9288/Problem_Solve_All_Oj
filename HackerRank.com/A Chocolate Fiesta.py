n = int(input())
arr = list(map(int,input().split()))[:n]
even = 0
odd = 0
for item in arr:
    if item % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1
x = pow(2, even)
if odd == 0:
    y = 1
else:
    y = pow(2, odd - 1)
print(((x*y)-1)%((pow(10,9) + 7)))
