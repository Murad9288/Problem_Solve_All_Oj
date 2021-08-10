T = int(input())
for i in range(T):
    N = int(input())
    C = N % 10   # last digit nirnoy
    while N > 0:
        N = N //10   # first digit nirnoy
        if (N<10):
            print("Sum = %d"%(C+N)) # last digit + first digit
            break

