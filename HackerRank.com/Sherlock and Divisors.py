for _ in range(int(input())):
    n = int(input())
    c = 0
    for i in range(1,int((n**0.5))+1):
        if n%i == 0 and i%2 == 0:
            c += 1
        if n%(n//i) == 0 and (n//i)%2 == 0:
            c += 1
        if i == (n//i) and i%2 == 0 and n%i == 0:
            c -= 1
    print(c)
