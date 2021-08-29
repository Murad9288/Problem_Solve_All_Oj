# First code:
# Accepted code:

def is_Prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n > 2 and n % 2 == 0:
        return False
    root = int((n ** 0.5))
    for i in range(3, root+1, 2):
        if n % i == 0:
            return False
    return True
if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        res = is_Prime(n)
        if res:
            print("%d is a prime"%n)
        else:
            print("%d is not a prime" %n)

# second conde:
# But Not Accepted:
# Time limiet Exd.
'''
import math
for _ in range(int(input())):
    N = int(input())
    s = math.sqrt(N)
    if N == 2:
        print("%d is a prime"%N)
    elif N>1:
        for i in range(2,int(s)+1):
            if N%i == 0:
                print("%d is not a prime"%N)
                break
        else:
            print("%d is a prime"%N)
    else:
        print("%d is not a prime"%N)

'''


