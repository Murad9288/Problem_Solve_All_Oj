T = int(input())
N = []
for i in range(1000):
    j = 0
    while j < T:
        N.append(j)
        j = j + 1
    print("N[%d] = %d"%(i,N[i]))
