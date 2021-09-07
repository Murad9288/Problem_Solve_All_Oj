n = int(input())
s = str(input())
count = len(s)
for i, char in enumerate(s):
    index = None
    for j in range(i+1, n):
        if char == s[j]:
            if index is None:
                count +=1
            elif j - index == index - i:
                count += 1
                break
        else:
            if index is None:
                index = j
            else:
                break
print(count)
