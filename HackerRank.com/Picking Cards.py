mod = 1000000007
def solve(n):
    s = list(map(int, input().split()))
    p = [0]*(n+1)
    MAX = max(s)
    for i in s:
        p[i] += 1
    ans = 1
    num = 0
    for i in range(MAX+1):
        num += p[i]
        ans = ans*num % mod
        num -= 1
    while num > 0:
        ans = ans*num % mod
        num -= 1
    print(ans)
for _ in range(int(input())):
    solve(int(input()))
