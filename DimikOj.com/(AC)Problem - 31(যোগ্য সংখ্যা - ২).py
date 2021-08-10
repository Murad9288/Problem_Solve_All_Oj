T = int(input())
for t in range(T):
    list = [6, 28, 496, 8128, 33550336]
    num = int(input())
    for i in list:
        if i <= num:
            print(i)
    if t < T - 1:
        print()
