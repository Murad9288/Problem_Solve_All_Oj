h, m = map(int,input().split())
if h>10 or m>60 or h<0 or m<0:
    print("Wrong")
if h == 12:
    h = 0
if m == 60:
    m = 0
# ghorir Hours er kata proti minute er kon utponno kore o.5 degree *( h (value) *koto minute a 1 hours + m(value))
Hours_angle = 0.5*(h*60+m)
# Proti minute 6 degree kon utponno kore...
Minute_angle = 6*m
big_angle = Hours_angle-Minute_angle # eita holo sompurno angle ti nirnoy kore...
real_angle = min(360-big_angle,big_angle) # eita holo half angleti nirnoy kore..
print("%0.7f"%real_angle)
