li = []
for i in range(20):
    n = int(input())
    li.append(n)
c = 0
for j in li[::-1]:
    print("N[%d] = %d" %(c,j))
    c += 1
