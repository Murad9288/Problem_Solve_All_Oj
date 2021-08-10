def compute_lcm(x, y):
   if x > y:
       greater = x
   else:
       greater = y
   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1
   return lcm

for _ in range(int(input())):
     x,y = map(int,input().split())
     print("LCM =",compute_lcm(x, y))
