s = str(input())
d = "0123456789"
a = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
for i in s:
    if i in d:
        print("Digit")
        break
    elif i in a:
        print("Alphabet")
        break
    else:
        print("Special Character")
        break
