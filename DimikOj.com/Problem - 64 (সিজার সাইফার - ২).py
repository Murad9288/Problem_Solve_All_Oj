S = input()
s = int(input())
for i in S:
    if i == ' ':
        print(" ",end="")
        continue
    n = ord(i)
    c_n = 0
    if n <= 90:
        result = (n - 65 - s)%26
        c_n = result + 65
    elif (n <= 122) and (n >= 97):
        result = (n - 97 - s) % 26
        c_n = result + 97
    print(chr(c_n),end='')
    
