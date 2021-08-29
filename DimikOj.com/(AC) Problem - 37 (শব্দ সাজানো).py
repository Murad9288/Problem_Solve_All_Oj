T = int(input())
list = []
for _ in range(T):
    s = str(input())
    list.append(s)
list.sort()
for i in list:
    print(i)
