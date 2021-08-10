for _ in range(int(input())):
    sm_1 = 1
    sm_2 = 1
    s1,s2 = map(str,input().split())
    for i in s1:
        sm_1 *= ord(i)
    for j in s2:
        sm_2 *= ord(j)
    if sm_1%97 == sm_2%97:
        print("YES")
    else:
        print("NO")
