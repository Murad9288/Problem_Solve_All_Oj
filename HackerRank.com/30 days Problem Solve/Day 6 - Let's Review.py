#simple input:
'''
2
Hacker
hello
'''
#simple output:
'''
Hce akr
hlo el
'''

t = int(input())
for k in range(t):
     s = input()
     for i in range(len(s)):
          if i % 2 == 0:
               print(s[i],end="")
     print(end=" ")
     for i in range(len(s)):
          if i % 2 != 0:
               print(s[i],end="")
     print()
