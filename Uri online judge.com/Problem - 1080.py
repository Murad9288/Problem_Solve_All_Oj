L = []
for _ in range(100):
    n = int(input())
    L.append(n)
count = 0
for i in range (len(L)):
    if L[i]== max(L):
        count += i
        break
print(max(L))
print(count+1)
