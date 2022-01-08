a,b = map(int,input().split())
x = str(a)[::-1]
y = str(b)[::-1]
print(max(int(x),int(y)))
