#Sample Input:
'''
7
0 0 1 0 0 1 0
'''
# Sample Output:
'''
4
'''
n = int(input())
c = list(map(int,input().strip().split()))
c.insert(n,0)
count = 0
i = 0 
while i < n - 1:
    if i < n-2 and c[i+2] == 0:
        i += 2
    else:
        i += 1
    count += 1
print (count)
