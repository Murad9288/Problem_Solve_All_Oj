s = 0
c = 0
while True:
    n = int(input())
    if n<0:
        break
    else:
        s += n
        c += 1
print("%.2f"%(s/c))
