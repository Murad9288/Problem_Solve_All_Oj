par = []
impar = []
for i in range(15):
    n = int(input())
    if n%2==0:
        par.append(n)
    else:
        impar.append(n)
    if len(par) == 5:
        count = 0
        for j in par:
            print("par[%d] = %d"%(count,j))
            count += 1
        par = []
    if len(impar) == 5:
        count = 0
        for j in impar:
            print("impar[%d] = %d"%(count,j))
            count += 1
        impar = []
if len(impar) > 0:
    count = 0
    for j in impar:
        print("impar[%d] = %d"%(count,j))
        count += 1
if len(par) > 0:
    count = 0
    for j in par:
        print("par[%d] = %d"%(count,j))
        count += 1
