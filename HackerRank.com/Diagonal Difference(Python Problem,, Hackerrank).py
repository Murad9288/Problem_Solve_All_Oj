N = int(input())
total = 0
for i in range(N):
    row = input().split()
    total += int(row[i])-int(row[-(i+1)])
print(abs(total))
