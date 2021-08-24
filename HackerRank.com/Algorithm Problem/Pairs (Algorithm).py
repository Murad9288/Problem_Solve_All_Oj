n, m = map(int,input().split())
arr = list(map(int,input().split()))
arr_set = set(arr)
count = 0
for i in arr_set:
    if(i+m in arr_set):
        count += 1
print(count)
