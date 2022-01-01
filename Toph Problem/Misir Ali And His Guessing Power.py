n,k = map(int,input().split())
arr = list(map(int,input().split())) [:k]
count = 0
for i in arr:
    if i>=k:
        count += 1
res = len(arr)/2
if res<=count:
    print("Misir Ali is absolutely correct.")
else:
    print("Oops! Misir Ali is wrong.")
