sd,sn = input().split()
sn = int(sn)
h,m,s = map(int,input().split(" : "))
ed,en = input().split()
en = int(en)
h1,m1,s1 = map(int,input().split(" : "))
count = 0
count += (en-sn-1)*86400
s_time = (h*3600) + (m*60) + s
count += 86400 - s_time
count += (h1*3600) + (m1*60) + s1
rd = count // 86400
count %= 86400
rh = count // 3600
count %= 3600
rm = count // 60
rs = count % 60
print("%d dia(s)"%rd)
print("%d hora(s)"%rh)
print("%d minuto(s)"%rm)
print("%d segundo(s)"%rs)
