def towerBreakers(n, m):
    if n%2 == 0 or m == 1:
        return 2
    else:
        return 1

if __name__ == '__main__':
    for _ in range(int(input())):
        n,m = map(int,input().split())
        print(towerBreakers(n,m))
