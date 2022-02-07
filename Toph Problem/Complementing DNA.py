for _ in range(int(input())):
    s = str(input())
    ss = ""
    for i in s.upper():
        if i == "A":
            ss += "T"
        elif i == "C":
            ss += "G"
        elif i == "G":
            ss += "C"
        elif i == "T":
            ss += "A"
    print(ss[::-1])
