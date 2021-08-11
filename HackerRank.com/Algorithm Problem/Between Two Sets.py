# 1st rules:

n,m = map(int,input().rstrip().split())
arr = list(map(int,input().split()))
brr = list(map(int,input().split()))
arr.sort()
brr.sort()
result = 0
# first step:
for i in range(brr[0]+1):
    if i >= arr[-1]:
        for j in range(n):
            if i % arr[j] != 0:
                break
            # second step
            if j == n-1:
                for k in range(m):
                    if brr[k] % i != 0:
                        break
                    if k == m-1:
                        result += 1
print(result)

# Second rules:
'''
n,m = map(int,input().rstrip().split())
arr = list(map(int,input().split()))
brr = list(map(int,input().split()))
maxA = max(arr)
minB = min(brr)
count = 0
for i in range(maxA,minB+1):
    if all([i%j == 0 for j in arr]):
        if all([j%i == 0 for j in brr]):
            count += 1
print(count)

'''
# Third rules:
'''
n,m = map(int,input().rstrip().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
candidates = range(max(a), min(b)+1)
results = list(candidates)
for c in candidates:
    for i in a:
        if c in results and c % i != 0:
            results.remove(c)
            break
    for i in b:
        if c in results and i % c != 0:
            results.remove(c)
            break
print(len(results))

'''


