while True:
    x,y = map(int,input().split())
    if x>y:
        print("Decrescente")
    elif x==y:
        break
    else:
        print("Crescente")
