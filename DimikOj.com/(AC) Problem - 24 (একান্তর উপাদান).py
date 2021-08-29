for _ in range(int(input())):
    n = int(input())
    array = list(map(int,input().split()))
    count = []
    for i in range(len(array)):
        if i % 2 == 0:
            count.append(array[i])
    print(*count)
