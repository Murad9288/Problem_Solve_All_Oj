import re
for _ in range(int(input())):
    try:
        s = str(input())
        print(bool(re.compile(s)))
    except:
        print(False)
