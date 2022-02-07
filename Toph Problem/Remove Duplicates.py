for t in range(int(input())):
    chars = str(input())
    s = []
    for i in chars:
        if i not in s:
            s.append(i)
    print("Case #%d:"%(t+1))
    for char in s:
        c = chars.count(char)
        print(char,c)
