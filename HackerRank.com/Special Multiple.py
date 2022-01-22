for _ in range(int(input())):
    n = int(input())
    i = 1
    while True:
        b = int(bin(i)[2:])*9
        if b%n == 0:
            print(str(b))
            break
        else:
            i += 1
            continue
