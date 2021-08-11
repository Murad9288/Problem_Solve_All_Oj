n = int(input().strip())
li  = list(map(int,input().split()))
n = max(li)
c = []
for i in li:
     if i == n:
          c.append(i)
print(len(c))

# simple input..
'''
4
3 2 1 3
'''
# simple output...
'''
2
'''
