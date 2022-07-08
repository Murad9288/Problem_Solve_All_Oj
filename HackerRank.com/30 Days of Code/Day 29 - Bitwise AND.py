# First Rules:
# Accepted:

'''
def Bitwiseand(n,k):
    max = 0
    for i in range(k-2,n):
        for j in range(i+1, n+1):
            res = i & j
            if res == k-1:
                return res
            if max<res<k:
                max = res

    return max

for _ in range(int(input().strip())):
    n, k = map(int,input().split())
    print(Bitwiseand(n,k))
'''
# Second Rules:
# Accepted:

T = int(input().strip())
for _ in range(T):
    n , k = map(int , input().split())
    if ((k-1) | k) <= n:
         print(k-1)
    else:
        print(k-2)
              
