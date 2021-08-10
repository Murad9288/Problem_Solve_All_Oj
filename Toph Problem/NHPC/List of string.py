A,B,C = map(int,input().split())
N = int(input())
a_1 = 0
b_1 = 0
c_1 = 0
for i in range(N):
    S,li = map(int,input().split())
    if (S == 1 and li == 2):
        A, B = B, A
        if A == 1:
            a_1 += 1
        elif B ==1:
            b_1 += 1
        else:
            c_1 += 1
    elif (S == 1 and li == 3):
        A,C = C,A
        if A == 1:
            a_1 += 1
        elif C == 1:
            c_1 += 1
        else:
            b_1 += 1
    elif (S == 2 and li == 3):
        B,C = C, B
        if B == 1:
            b_1 += 1
        if C == 1:
            c_1 += 1
        else:
            a_1 += 1
print("%d %d %d"%(a_1,b_1,c_1))
