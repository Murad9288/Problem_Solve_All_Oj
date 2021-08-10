n = int(input())
h = n//3600
m = n//60
s = n%60
if m < 60:
    print("%d:%d:%d"%(h,m,s))
else:
    print("%d:%d:%d"%((h,(m%60),s)))
