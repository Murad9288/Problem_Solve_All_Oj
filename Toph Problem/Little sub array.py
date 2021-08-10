N,A,B = map(int,input().split())
list1 = list(map(int,input().split()))
total = 0
for i in list1[A:(B+1)]:
    total += i
print(total)
