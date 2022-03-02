for _ in range(int(input())):
    a, b, c = map(int, input().split())
    print((a * b * c) % (10 ** 9 + 7))
