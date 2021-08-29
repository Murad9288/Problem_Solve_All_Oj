# Accepted code:
for _ in range(int(input())):
    a,b = map(int,input().split())
    li = [False if x%2 == 0 else True for x in range(100002)]
    li[1] = False
    li[2] = True
    for i in range(3,int(100002**0.5),2):
        for j in range(i*i,100002,i):
            li[j] = False
    count = 0
    for i in range(a,b+1):
        if li[i]:
            count += 1
    print(count)



# ei codeta time limit khai..
'''
for _ in range(int(input())):
    a,b = map(int,input().split())
    count = []
    for j in range(a,b):
        for k in range(2,j):
            if j%k == 0:
                print(k)
                break
        else:
            count.append(j)
    print(len(count))
'''
