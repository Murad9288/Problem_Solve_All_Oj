def dimik(n):
    if n%2==0:
        return("even")
    else:
        return("odd")
T=int(input())
for i in range(T):
    n=int(input())
    print(dimik(n))
