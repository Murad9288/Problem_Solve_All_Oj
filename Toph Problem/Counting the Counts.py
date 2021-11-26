n = int(input())
li = list(map(int,input().split())) [:n]
c = 0
for i in li:
      if i<=100 and i>=80:
            c += 1
print(c)
