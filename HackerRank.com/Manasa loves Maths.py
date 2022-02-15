from itertools import permutations as pr


def solve(n):
    p = list(pr(n, 3))
    for i in p:
        if (int(''.join(i)) % 8 == 0):
            return 1
    return 0


for _ in range(int(input())):
    n = input()
    if len(n) <= 2:
        n = list(n)
        if len(n) == 1 and int(''.join(n)) % 8 == 0:
            print('YES')
        elif len(n) == 2 and (int(''.join(n)) % 8 == 0 or int(''.join(reversed(n))) % 8 == 0):
            print('YES')
        else:
            print('NO')
        continue
    if solve(n):
        print('YES')
    else:
        print('NO')
