import math
T = int(input())
for i in range(1,T+1):
        n = int(input())
        s = int(math.sqrt(n))
        if s*s == n:
            print("YES")
        else:
            print("NO")
                        
                
        
