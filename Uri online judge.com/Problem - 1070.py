X = int(input())
count = 0
while count<6:
    if X%2==1:
        print(X)
    else:
        print(X+1)
    count += 1
    X += 2
