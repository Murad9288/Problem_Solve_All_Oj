# 1st system:
#Accepted:
import sys
import string
symbols_low = string.ascii_lowercase
symbols_up = string.ascii_uppercase

def caesarCipher(s, k):
    res = []
    for c in s:
        if c.isupper():
            res.append(symbols_up[(symbols_up.index(c)-k)%len(symbols_up)])
        elif c.islower():
            res.append(symbols_low[(symbols_low.index(c)-k)%len(symbols_low)])
        else:
            res.append(c)

    return "".join(map(str, res))


if __name__ == "__main__":
    k = int(input().strip())
    s = input().strip()
    result = caesarCipher(s, k)
    print(result)
# second system:
# Not Accepted:
'''
n=int(input())
input_string=input()

list1=input_string.split(' ')
list2=[]
for item in list1:
    list2.append(" ")
    for ch in item:
        list2.append(chr(ord(ch)-2))

output_string=''.join(list2)
print(output_string.strip())
'''
