# 1st System:
def caesarCipher(s, k):
    if k == 0:
        return s
    new_s = []
    for i in range(len(s)):
        c = s[i]
        if c.isalpha():
            c = (ord(c) + k - 97)%26 + 97 if c.islower() else (ord(c) + k - 65)%26 + 65
            c = chr(c)
        new_s.append(c)
    return ''.join(new_s)

# Driver code:
if __name__ == "__main__":
    n = int(input())
    s = input().strip()
    k = int(input().strip())
    
    result = caesarCipher(s, k)
    print(result)

# Second System:
'''
import sys
import string
symbols_low = string.ascii_lowercase
symbols_up = string.ascii_uppercase

def caesarCipher(s, k):
    res = []
    for c in s:
        if c.isupper():
            res.append(symbols_up[(symbols_up.index(c)+k)%len(symbols_up)])
        elif c.islower():
            res.append(symbols_low[(symbols_low.index(c)+k)%len(symbols_low)])
        else:
            res.append(c)

    return "".join(map(str, res))


if __name__ == "__main__":
    n = int(input())
    s = input().strip()
    k = int(input().strip())
    
    result = caesarCipher(s, k)
    print(result)
'''
