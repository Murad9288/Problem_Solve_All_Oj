import bisect

for test_cases in range(int(input().strip())):
    n, m = map(int, input().strip().split())
    arr = list(map(int, input().strip().split()))
    prefix, mx = 0, 0
    st = []
    for i in arr:
        prefix = (prefix + i) % m
        mx = max(mx, prefix)
        index = bisect.bisect_left(st, prefix + 1)
        if index < len(st):
            mx = max(mx, prefix - st[index] + m)
        bisect.insort(st, prefix)
    print(mx)
