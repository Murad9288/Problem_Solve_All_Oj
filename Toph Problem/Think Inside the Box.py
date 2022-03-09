def solve(n):
    s = []
    while n:
        s.append(n%10)
        n //= 10
    return len(set(s)) == 1
n = int(input())
for i in range(n,0,-1):
    if solve(i):
        print(i)
        break
