# First Rules:

for _ in range(int(input())):
    x,n = map(int,input().split())
    count = 0
    for i in range(n+1):
        count += x**i
    print("Result = %d"%count)

# Second Rules:
'''
for _ in range(int(input())):
     a,b = map(int,input().split())
     sum = 1
     power = 1
     for i in range(1,b+1):
          power *= a
          sum += power
     print("Result = %d"%sum)
'''
