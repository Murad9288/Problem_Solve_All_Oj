n = int(input())
arr = list(map(int,input().split()))
Set = set(arr)
c_arr = []
for i in Set:
    c_arr.append(arr.count(i))
max_n = max(c_arr)
result = list(Set)[c_arr.index(max_n)]
print(result)
