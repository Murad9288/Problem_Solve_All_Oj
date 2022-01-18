n = int(input())
s = str(input())[:n]
a = s.count("N")
b = s.count("S")
c = s.count("U")
if a<b and a<c:
    print(a)
elif b<a and b<c:
    print(b)
else:
    print(c)
