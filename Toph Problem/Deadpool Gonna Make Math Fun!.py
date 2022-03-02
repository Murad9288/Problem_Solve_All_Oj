n = int(input())
arr = sorted(list(map(int,input().split()))[:n])
if arr[0] == 1 and arr[-1] > 0:
    print("Positive Numbers")
elif arr[0] == 0 and arr[-1] > 0:
    print("Non Negative Numbers")
elif arr[0] <= -1 and arr[-1] <= -1:
    print("Negative Numbers")
else:
    print("Real Numbers")
