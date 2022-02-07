n = int(input())
s = sum(map(int,str(n)))
c = 0
i = 1
while n != 1:
    i += 1
    if n%i == 0:
        n//= i
        c += sum(map(int,str(i)))
        i = 1
if s == c:
    print(1)
else:
    print(0)
