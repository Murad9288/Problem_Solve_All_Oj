# MD Murad Hossain
# Competitive Programmer.
# Gmail-->: muradhossainm01@gmail.com

n = int(input().strip())
stack = list()
S = ""
for _ in range(n):
    s = input().strip().split()
    op = int(s[0])
    if op in [1, 2, 3]:
        oprd = s[1]
    else:
        oprd = None

    if op == 1:
        # Insert
        stack.append(S)
        S += oprd
    elif op == 2:
        # Delete
        stack.append(S)
        k = int(oprd)
        S = S[:len(S) - k]
    elif op == 3:
        # Print
        k = int(oprd)
        print(S[k - 1])
    elif op == 4:
        # Undo
        S = stack.pop()
    else:
        print('Invalid Operation')
# Program Finished.
