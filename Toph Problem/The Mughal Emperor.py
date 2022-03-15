import math, sys
for i in sys.stdin:
    n = int(i)
    print(2*(n+1-2**int(math.log2(n+1)))+1)
