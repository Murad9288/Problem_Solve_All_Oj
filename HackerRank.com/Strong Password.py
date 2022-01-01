n = int(input())
s = str(input()) # string input.
special = "!@#$%^&*()-+"

d = 0 # Digit
u = 0 # Upper_c
l = 0 # Lower_c
sp = 0 # Special_c
count = 0

for i in s:
    if i.isupper():
        u += 1
    elif i.islower():
        l += 1
    elif i.isdigit():
        d += 1
    elif i in special:
        sp += 1
        
if u == 0:
    count += 1
if l == 0:
    count += 1
if d == 0:
    count += 1
if sp == 0:
    count += 1
if u+l+sp+d+count < 6:
    count += (6-(u+l+sp+d+count))
print(count)
