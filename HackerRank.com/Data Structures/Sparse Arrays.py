#Accepted:
#Simple input:
'''
3
def
de
fgh
3
de
lmn
fgh
'''
#Simple Output:
'''
1
0
1
'''

s = []
for i in range(int(input())):
    string = input().split()
    s.append(string)
q = []
for j in range(int(input())):
    queries = input().split()
    q.append(queries)
result = []
for k in q:
    result.append(s.count(k))
for res in result:
    print(res)
