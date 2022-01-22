while(True):
    a = int(input())
    if a==0:
        break
    b = list(map(int,input().split()))
    z = [0]*len(b)
    for i in range(len(b)):
        z[b[i]-1]+=i+1
    if b==z:
        print('ambiguous')
    else:
        print('not ambiguous')
