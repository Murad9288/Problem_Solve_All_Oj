for k in range(int(input())):
    n = int(input())
    li = []
    for i in range(n):
        li.append(float(input()))
    print("Case %d: %.3f"%(k+1,(sum(li)/n)))
