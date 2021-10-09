X = int(input())
Y = int(input())
if Y < X:
    temp = X # biporit pasherta boro hole X er mantake Y er moddhe and Y er man ta ke X er moddhe newa lagbe..
    X = Y
    Y = temp
for i in range(X+1,Y):
    if i%5==2 or i%5==3:
        print(i)
