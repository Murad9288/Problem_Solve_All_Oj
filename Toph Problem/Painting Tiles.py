for t in range(int(input())):
    n = int(input())
    if n % 7 < 2:
        print("Case %d: Oh no, my eggs! :("%(t+1))
    else:
        print("Case %d: No eggs for you! :D"%(t+1))
