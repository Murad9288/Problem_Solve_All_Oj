arr =[1,2,3,5,6,7,10,11,14,15,19,23]
for _ in range(int(input())):
    a,b = map(int,input().split())
    if b>a:
        a,b = b,a # swaping
    c = (a-b)+1
    for i in arr:
        if i>=b and i<=a:
            c-=1
    print(c)
