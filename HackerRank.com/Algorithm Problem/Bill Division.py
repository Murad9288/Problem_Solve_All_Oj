#Sample Input 0:
'''
4 1
3 10 2 9
12
'''
#Sample Output 0:
'''
5
'''
#Sample Input 1:
'''
4 1
3 10 2 9
7
'''
#Sample Output 1:
'''
Bon Appetit
'''
# Programme Start:

f = input().rstrip().split()
n = int(f[0])
k = int(f[1])
bill = list(map(int, input().rstrip().split()))
b = int(input().strip())
discount = bill[k]
total = sum(bill)
res = (total - discount) // 2
if res != b:
     print(b - res)
else:
     print('Bon Appetit')
