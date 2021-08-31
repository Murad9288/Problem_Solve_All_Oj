for _ in range(int(input())):
    x,y,z = map(float,input().split())
    avg = ((x/10)*2 + (y/10)*3 + (z/10)*5)
    print("%.1f"%avg)
