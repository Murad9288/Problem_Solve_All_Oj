N = int(input())
li = list(map(int, input().split()))
for i in range(N):
     print(sum(li[:i+1])/(i+1))
