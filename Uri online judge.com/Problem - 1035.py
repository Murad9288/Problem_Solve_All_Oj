A,B,C,D = map(int,input().split())
if B>C and D>A and D>=0 and C>=0 and C+D>A+B and A%2 == 0:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")
'''
A,B,C,D = map(int,input().split())
if B>C and D>A:
    if C+D>A+B:
        if C>=0 and D>=0:
            if A%2==0:
                print("Valores aceitos")
            else:
                print("Valores nao aceitos")
        else:
            print("Valores nao aceitos")
    else:
        print("Valores nao aceitos")
else:
    print("Valores nao aceitos")
'''
