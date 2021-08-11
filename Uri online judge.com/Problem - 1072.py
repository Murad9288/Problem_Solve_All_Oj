N = int(input())
interval = 0
non_interval = 0
for _ in range(N):
    X = int(input())
    if X>=10 and X<=20:
        interval += 1
    else:
        non_interval += 1
print("%d in"%interval)
print("%d out"%non_interval)
