import math
def n_c(n,k):
    return math.factorial(n)//(math.factorial(k)*math.factorial(n-k))
def solve(n,k):
    return n_c(n+k-1,k)%10**9
for _ in range(int(input())):
    n = int(input())
    k = int(input())
    print(solve(n,k))
