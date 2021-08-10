# Accepted:
for _ in range(int(input())):
    S = str(input())
    c = 0
    for i in S:
        if i=="O":
            c += 1
        elif i=="W" or i=="N" or i=="D":
            continue
        elif i=="0" or i =="1" or i =="2" or i =="3" or i =="4" or i =="5" or i =="6":
                c += 1
    if c == 6:
        print("1 OVER")
    elif  c<6:
        print("%d BALLS"%c)
    else:
        if c//6 == 1:
            if c%6==1:
                print("%d OVER %d BALL"%(c//6,c%6))
            else:
                print("%d OVER %d BALLS"%(c//6,c%6))
        elif c>7 and c%6 == 0:
             print("%d OVERS"%(c//6))
        else:
            print("%d OVERS %d BALLS"%(c//6,c%6))
