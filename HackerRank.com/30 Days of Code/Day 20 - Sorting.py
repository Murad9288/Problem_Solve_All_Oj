N = int(input())
L = list(map(int,input().split()))
swap = 0
for i in range(len(L)-1, 0,-1):
    for j in range(i):
        if L[j] > L[j+1]:
            L[j], L[j+1] = L[j+1], L[j]
            swap += 1
print("Array is sorted in %d swaps."%swap)
print("First Element: %d"%(L[0]))
print("Last Element: %d"%(L[-1]))
