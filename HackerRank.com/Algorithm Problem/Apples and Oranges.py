#Sample Input:
'''
7 11
5 15
3 2
-2 2 1
5 -6
'''
#Sample Output:
'''
1
1
'''
st = input().split()
# eikhane st variable ke vange single kore nite hobe...
s = int(st[0])
t = int(st[1])
ab = input().split()
a = int(ab[0])
b = int(ab[1])
mn = input().split()
m = int(mn[0])
n = int(mn[1])
apples = list(map(int,input().split()))
oranges = list(map(int,input().split()))
count_a = 0
count_b = 0
for i in apples:
     if i+a >= s and i+a <= t:
          count_a += 1
print(count_a)
for j in oranges:
     if j+b >= s and j+b <= t:
          count_b += 1
print(count_b)
