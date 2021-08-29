while True:
    n = int(input())
    if n == 0:
        break
    result = n
    revility = int((n+1)**0.5)
    for i in range(2,revility+1):
        if n%i==0:
            while n%i==0:
                n = n/i
            result = result - (result/i)
    if n>1:
        result = result - (result/n)
    print(int(result))
