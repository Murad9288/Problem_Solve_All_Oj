import math
for _ in range(int(input())):
    a,b,c = map(int,input().split())
    res_1 = math.floor((a**b)/c)*c
    res_2 = math.ceil((a**b)/c)*c
    if (a**b)-res_1 < res_2-(a**b):
        print(res_1)
    else:
        print(res_2)
