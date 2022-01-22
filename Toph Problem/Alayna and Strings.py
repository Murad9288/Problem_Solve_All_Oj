s = str(input())
l = "abcdefghijklmnopqrstuvwxyz"
u = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
c_l = 0
c_u = 0
for i in s:
    if i in l:
        c_l += 1
    elif i in u:
        c_u += 1
print(c_u,c_l)
