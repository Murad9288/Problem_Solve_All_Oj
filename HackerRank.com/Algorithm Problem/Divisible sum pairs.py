# Sample Input:
'''
6 3
1 3 2 6 1 2
'''
# Sample Output:
'''
5
'''

n,k = map(int,input().rstrip().split())
arr = list(map(int,input().rstrip().split()))
r = 0
for i in range(n-1):
     for j in range(i+1,n):
          if (arr[i]+arr[j])%k == 0:
               r += 1
print(r)
