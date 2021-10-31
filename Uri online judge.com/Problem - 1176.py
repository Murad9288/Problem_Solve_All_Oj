new_list=[0,1]
c = 0
t = 1
for i in range(60):
    temp = t+c
    new_list.append(temp)
    c = t
    t = temp
n = int(input())
for i in range(n):
    n = int(input())
    print('Fib(%d) = %d' %(n,new_list[n]))
