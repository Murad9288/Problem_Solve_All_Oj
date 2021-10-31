L = int(input())
T = input()
s = 0
for i in range(12):
    for j in range(12):
        f = float(input())
        if L==i:
            s += f
if T == 'S':
    print("%.1f"%s)
else:
    print("%.1f"%(s/12))
