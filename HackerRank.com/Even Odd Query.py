n = int(input())
arr = list(map(int,input().split()))[:n]
q = []
for _ in range(int(input())):
    q.append(list(map(int,input().split())))
result = []
for i,j in q:
    if(i<len(arr) and arr[i]== 0 and i!=j):
        result.append("Odd")
    else:
        if(arr[i-1]%2==0):
            result.append("Even")
        else:
            result.append("Odd")
for r in result:
    print(r)
