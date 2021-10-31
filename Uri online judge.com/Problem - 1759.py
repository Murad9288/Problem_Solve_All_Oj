n = int(input())
s = ""
for i in range(n):
    s += "Ho"
    if i == n-1:
        s += "!"
    else:
        s += " "
print(s)
