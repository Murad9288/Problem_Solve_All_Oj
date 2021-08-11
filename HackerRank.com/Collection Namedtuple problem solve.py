from collections import namedtuple
n = int(input())
data = namedtuple("data",input().split())
s = 0
for i in range(n):
    s += int(data(*input().split()).MARKS)
print(s / n)
