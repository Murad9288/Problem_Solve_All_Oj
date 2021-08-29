# First System:

for _ in range(int(input())):
    s = input()
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numeric = "0123456789"
    for char in s:
        if char in lower:
            print("Lowercase Character")
            break
        elif char in upper:
            print("Uppercase Character")
            break
        elif char in numeric:
            print("Numerical Digit")
            break
        else:
            print("Special Character")
            break
        
# Second System:
'''
for _ in range(int(input())):
    s = input()
    if s.islower() == True:
        print("Lowercase Character")
    elif s.isupper() == True:
        print("Uppercase Character")
    elif s.isdigit() == True:
        print("Numerical Digit")
    else:
        print("Special Character")
'''
