count = 1
for i in range(1000,0,-1):
    print(i, end=" ")
    if count == 5:
        print()
        count = 0
    count += 1
    
