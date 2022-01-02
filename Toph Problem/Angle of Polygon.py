for _ in range(int(input())):
    n = int(input())
    if n<3:
        print(0)
    else:
        print("%.6f"%((1-(2.0/n))*180)) 
