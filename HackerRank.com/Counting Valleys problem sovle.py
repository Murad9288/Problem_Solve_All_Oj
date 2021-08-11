# Sample Input:
'''
8
UDDDUDUU
'''
# Sample Output:
'''
1
'''
n = int(input().strip())
s = input().strip()
valleys = 0
level = 0
for i in s:
    if i == 'U':
        if level == -1:
            valleys += 1
        level += 1
    elif i == 'D':
        level -= 1
print(valleys)
