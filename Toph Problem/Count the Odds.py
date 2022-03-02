def solve(n):
    if n & 1:
        return (n//2+1)
    else:
        return (n//2)
a,b = map(int,input().split())
print(solve(b)-solve(a-1))
