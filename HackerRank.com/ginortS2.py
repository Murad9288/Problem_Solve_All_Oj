a,b,c,d=[],[],[],[]
for i in sorted(str(input())):
    if i.isalpha():
        if i.isupper():
            x = b
        else:
            x = a
    else:
        if int(i) % 2:
            x = c
        else:
            x = d
    x.append(i)
print("".join(a+b+c+d))
