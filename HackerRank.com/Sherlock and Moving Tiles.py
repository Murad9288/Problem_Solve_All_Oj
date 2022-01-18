import math
a, b, c = map(int,input().split())
for _ in range(int(input())):
    n = int(input())
    res = math.sqrt(2)*(a-math.sqrt(n))/abs(c-b)
    print (res)
