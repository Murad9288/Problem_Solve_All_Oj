import numpy as np

a=input()

n=len(a)
x=[0]*n
a=int(a)
for i in range(0,n):
    f=a//1000
    r=a%1000
    
    if r!=0:
        x[i]=r
        a=f
x=np.trim_zeros(x)
x.reverse()
p=",".join(str(i) for i in x)
print (p)
