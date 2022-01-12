for _ in range(int(input())):
    n = int(input())
    arr = []
    for i in str(n):
        arr.append(int(i))
    print(len(set(arr)))
