count = 1
for i in range(1000,0,-1):
    print(i,end='\t')
    if count == 5:
        print()
        count = 0
    count = count+1
    
