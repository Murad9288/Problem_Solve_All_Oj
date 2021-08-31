for _ in range(int(input())):
    n = int(input())
    if n>0 and n%2 == 0:
        print("EVEN POSITIVE")
    elif n == 0:
        print("NULL")
    elif n>0 and n%2 == 1:
        print("ODD POSITIVE")
    elif n<0 and n%2 == 1:
        print("ODD NEGATIVE")
    else:
        print("EVEN NEGATIVE")
