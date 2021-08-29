# Accepted:

for _ in range(int(input())):
    n = int(input())
    s = []
    for i in range(n, -1, -1):
        if i == 1:
            s.append("2 +")
        elif i == 0:
            s.append("1")
        else:
            s.append("2^%d +"%i)
    print(*s)

# Right. But not submit:
'''
for _ in range(int(input())):
    n = int(input())
    for i in range(n, -1, -1):
        if i == 1:
            print("2 + ",end="")
        elif i == 0:
            print("1",end="")
        else:
            print("2^%d + "%i, end="")
    print()
            
'''
#wrong answer:
'''
for _ in range(int(input())):
    n = int(input())
    c = []
    for i in range(n,-1,-1):   
        x = "2^%d +"%i
        c.append(x)
    print(*c,"2 + 1") 
'''
