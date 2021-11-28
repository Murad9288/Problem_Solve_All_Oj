n = int(input())
li = list(map(int,input().split())) [:n]
m = 0
for i in li:
    count_1 = li.count(i)
    count_2 = li.count(i-1)
    count_1 += count_2
    if count_1 > m:
        m = count_1
print(m)
