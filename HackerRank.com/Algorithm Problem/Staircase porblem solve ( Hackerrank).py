'''
# simple input - output:
6
      #        #output..
    ##
   ###
  ####
 #####
######
'''
# First System..
'''
n = int(input())
for i in range(n):
    for j in range(n-i-1):
        print(end=' ')
    for j in range(i+1):
        print('#',end='')
    print()
'''
# Second System..
'''
n = int(input())
for i in range(1, n + 1):
        print(str('#'*i).rjust(n))
'''
# Third System..

n = int(input())
print('\n'.join([' '*(n-x)+'#'*x for x in range(1,n+1)]))

# rjust er example:

t = "Murad____"
print(t.rjust(13,"_"))

