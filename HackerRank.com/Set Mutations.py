n = int(input())
a = set(map(int,input().split()))
for _ in range(int(input())):
    c, newSet = (input().split()[0],set(map(int,input().split())))
    getattr(a, c)(newSet)
print (sum(a))
