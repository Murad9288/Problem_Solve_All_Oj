# 1st rules:
print(''.join(str(ord(i)-64) for i in input()))

#Dimikoj Accept
# 2nd rules:

for i in range(int(input())):print(''.join(str(ord(ch)-64) for ch in input()))

#  3rd Rules:
for T in range(int(input())):
    t = input()
    for ch in t:
        print(ord(ch) - 64, end='')
    print()
    
# 4th Rules:
for _ in range(int(input())):
    s = input()
    list = []
    for char in s:
        count = ord(char)-64
        list.append(count)
    for k in list:
        print(k,end='')
    print()
