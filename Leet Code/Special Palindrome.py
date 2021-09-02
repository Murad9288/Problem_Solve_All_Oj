n = int(input())
if n>=0:
    L = str(n)
    if L == L[::-1]:
        print("True")
    else:
        print("False")
else:
    x = abs(n)
    b = str(x)[::-1]
    r = int(b)*(-1)
    if r == n:
        print("True")
    else:
        print("False")
