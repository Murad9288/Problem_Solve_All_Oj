T = int(input())
for i in range(T):
        N = int(input())
        factorial = 1
        for j in range(1,N+1):
                factorial = factorial*j
        print(factorial)
