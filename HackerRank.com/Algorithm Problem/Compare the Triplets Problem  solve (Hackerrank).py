# simple input - output:
'''
1 2 3
3 2 1
1 1 # Output

17 28 30
99 16 8
2 1 # Output
'''
a = list(map(int,input().split()))

b = list(map(int,input().split()))
alice = 0
bob = 0

for i in range(len(a)):
    if a[i] > b[i]:
        alice += 1

for j in range(len(b)):
    if b[j] > a[j]:
        bob += 1

result = (alice,bob)
print(' '.join(map(str,result)))
