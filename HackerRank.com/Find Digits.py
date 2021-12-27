for _ in range(int(input())):
    n = int(input())
    c = 0
    for i in str(n):
        if int(i) != 0 and n%int(i) == 0:
            c += 1
    print(c)

"""
  # Problem Create:
    
    for t in range(int(input())):
    n = int(input())
    count = 0
    for i in str(n):
        if int(i) != 0 and n%int(i) == 0:
            count += 1
    print("Case %d: %d"%(t+1,count))
    
    
"""
