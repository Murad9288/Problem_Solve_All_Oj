def main():
    n = int(input())
    return n

def his_kits(n):
    s = 0
    for i in range(n):
        s += i
    s -= n
    print(s)

his_kits(main())
