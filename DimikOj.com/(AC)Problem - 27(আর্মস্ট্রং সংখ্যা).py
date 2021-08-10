T = int(input())
for i in range(T):
    n = int(input())
    sum = 0
    d = n
    while d > 0:
        digit = d % 10
        sum += digit ** 3
        d //= 10
    if n == sum:
        print(n,"is an armstrong number!")
    else:
        print(n,"is not an armstrong number!")
