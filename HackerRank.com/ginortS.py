s = list(input())
low = []
up = []
odd = []
even = []

li = []
    
for i in range(len(s)):
    if s[i].islower() and s[i].isalpha():
        low.append(s[i])
    elif s[i].isupper() and s[i].isalpha():
        up.append(s[i])
    elif s[i].isdigit():
        s[i] = int(s[i])
        if s[i]%2 == 0:
            even.append(s[i])
        else:
            odd.append(s[i])

low.sort()
up.sort()
odd.sort()
even.sort()
li.extend(low)
li.extend(up)
li.extend(odd)
li.extend(even)

print("".join(str(j) for j in li))
