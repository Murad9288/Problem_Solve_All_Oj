for _ in range(int(input())):
    b,w = map(int,input().split())
    bc,wc,z = map(int,input().split())
    print((b*min(bc,wc+z))+(w*min(wc,z+bc)))
