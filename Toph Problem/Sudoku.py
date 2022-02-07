c = 0
for _ in range(9):
    s = str(input())
    if len(set(s)) == len(s):
        c += 1
if c == 9:
    print("Congratulations!")
else:
    print("Oh No!")
