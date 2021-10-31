for _ in range(int(input())):
    n = int(input())
    s = n//2
#   li = []
    c = 0
    for i in range(1,s+1):
        if n%i == 0:
        #   li.append(i)
            c += i
#   print(li) . Check number.
    if c == n:
        print("%d eh perfeito"%n)
    else:
        print("%d nao eh perfeito"%n)
