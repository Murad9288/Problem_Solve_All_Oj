n = int(input().strip())
array = list(map(int,input().rstrip().split()))
result = 0
for i in range(1,len(array)):
    for j in range(i):
        maximum = max(array[j:i + 1])
        if (array[j] * array[i] <= maximum):
            result += 1
print(result)
