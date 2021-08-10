#E
#E. Unique String
a =input()
s = a.lower()
c = []
li=["a","e","i","o","u"]
for char in s:
    if char in li:
        c.append(char)
if len(c) > 2 and len(s) <= 10:
    print("YES")
else:
    print("NO")
