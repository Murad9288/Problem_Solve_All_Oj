'''
for T in range(int(input())):
     s1 = set(input())
     s2 = set(input())
     result = s1.intersection(s2)
     if not result:
         print("NO")
     else:
         print("YES")
'''
# Second System..

for _ in range(int(input())):
     a = set(input())
     s = set(input())
     # intersection bebohar korar somoy oboshoy set() function use kora lagbe..
     result = a.intersection(s) # Eikhane 'intersections' er kaj holo common sonkha guloke check korbe.and count korbe.
     if not result:
         print('NO')
     else:
         print('YES')

