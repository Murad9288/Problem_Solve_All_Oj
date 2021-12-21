for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split())) [:n]
    c = 0
    q1 = 1
    q2 = 2
    q3 = 3
    for i in range(len(arr)):
        if arr[i] == q1:
            q1 = q2
            q2 = q3
            q3 += 1
        elif arr[i] == q2:
            c += 1
            q2 = q3
            q3 += 1
        elif arr[i] == q3:
            c += 2
            q3 += 1
        else:
            c = "Too chaotic"
            break
    print(c)
