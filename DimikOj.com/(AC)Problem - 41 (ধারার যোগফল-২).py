for _ in range(int(input())):
    n = int(input())
    sum = 0
    factorial = 1
    for i in range(1,n+1):
        factorial *= i
        sum += (i/factorial)
    print("%0.4f"%(sum))

