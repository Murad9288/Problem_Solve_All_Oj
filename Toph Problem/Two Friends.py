for t in range(int(input())):
    n = int(input())
    if n<=2:
        print("Case %d: Tie"%(t+1))
    else:
        if n&1:
            print("Case %d: CodeNewtons"%(t+1))
        else:
            print("Case %d: CodeMask"%(t+1))
