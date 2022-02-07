def to_dec(base, n):
    ans = 0
    for i in n:
        if int(i) >= base:
            return -1
        ans = (int(i)+ans*base)
    return ans
def solve(n):
    events = {}
    for _ in range(n):
        base, day = input().split()
        p = to_dec(int(base), day)
        if p != -1:
            events[p] = events.get(p, 0)+1
    ans = 0
    for i in events.values():
        ans += (i*(i-1)//2)
    print(ans)
n = int(input())
solve(n)
