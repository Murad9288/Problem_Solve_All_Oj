#simple input:
'''
3
'''
# simple output:
'''
  *
 * *
* * *

'''

N = int(input())
for i in range(1, N+1):
     result = ' '*(N-i)+' *'*i
     print(result[1:])

     #print(f"{' '*(n-i)}{' *'*i}"[1:])  # ei Formating diyew kora jay....
