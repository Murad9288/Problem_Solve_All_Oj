from itertools import product
a = list(map(int,input().split()))
b = list(map(int,input().split()))
print(*product(a,b))

# Diferrent Poddhotite..
'''from itertools import product
A = map(int,input().split())
B = map(int,input().split())
x = sorted(A)
y = sorted(B)

ans = [x,y]
r = list(product(*ans))
print(*r)'''

