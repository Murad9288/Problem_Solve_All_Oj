n = int(input())
if n%2 == 0:
    for i in range(n):
        if i%2 == 1:
            print(i)
else:
    for k in range(n+1):
        if k%2 == 1:
            print(k)
