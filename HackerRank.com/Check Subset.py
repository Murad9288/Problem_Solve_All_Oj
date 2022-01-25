for _ in range(int(input())):
    a = int(input())
    set_a = set(input().split())
    b = int(input())
    set_b = set(input().split())
    res_set = set_a.difference(set_b)
    if len(res_set) == 0:
        print(True)
    else:
        print(False)
