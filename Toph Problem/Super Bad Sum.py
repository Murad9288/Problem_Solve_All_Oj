def super_bad_sum(n):
    s = 0
    while n:
        r = n%10
        if r & 1:
            s += r
        n = n//10
    return s
for _ in range(int(input())):
    n = int(input())
    sum = 0
    if n>1:
        sum = 1
    else:
        sum = 0
    sum += super_bad_sum(n)
    for i in range(2,n+1):
        if n%i == 0:
            sum += super_bad_sum(i)
            if i*i != n:
                sum += super_bad_sum(n//i)
    print(sum//2)

