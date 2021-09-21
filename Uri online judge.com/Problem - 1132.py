a= int(input())
b = int(input())
t = a
s = 0
if(a > b):
    a = b
    b = t
while(a <= b):
    if(a%13 != 0):
        s += a
    a += 1
print(s)
