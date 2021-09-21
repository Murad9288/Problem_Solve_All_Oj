n=input()
li=[]
c=1
if len(n)==1:
    li.append((1,int(n)))
else:
    for i in range(len(n)-1):
        if n[i]==n[i+1]:
            c=c+1
        else:
            li.append((c,int(n[i])))
            c=1
    li.append((c,int(n[i+1])))
print(*li)
