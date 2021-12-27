for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    c = 0
    s = sum(arr)
    for i in arr:
        if c == s - c - i:
            print("YES")
            break
        else:
            c += i
    else:
        print("NO")
