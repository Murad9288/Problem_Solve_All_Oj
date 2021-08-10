for _ in range(int(input())):
    N = int(input())
    k = 0
    while 1 == 1:
        if N <= 2**k:
            break
        k += 1
    if N == 2**k:
        print("It's a power of 2")
    else:
        print("Not a power of 2")
