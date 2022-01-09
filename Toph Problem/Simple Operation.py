for t in range(int(input())):
    a,b,c = input().split()
    if b == "*":
        print("Case %d: %d"%(t+1,int(a)*int(c)))
    elif b == "-":
        print("Case %d: %d"%(t+1,int(a)-int(c)))
    elif b == "+":
        print("Case %d: %d"%(t+1, int(a)+int(c)))
