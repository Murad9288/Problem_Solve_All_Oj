n = int(input())
s = str(input())
a = s[::2]
b = s[1::2]
c = s.count("0")
c2 = s.count("1")
ca = a.count("0")
cb =  b.count("1")
ca2 = a.count("1")
cb2 = b.count("0")
if (ca == c and c2 == cb):
    print("No change needed")
elif c == cb and ca == c2:
    print("No change needed")
elif c == ca2 and c2 == cb2:
    print("No change needed")
elif c2 == ca2 and c == cb2:
    print("No change needed")
else:
    print("Change needed")
