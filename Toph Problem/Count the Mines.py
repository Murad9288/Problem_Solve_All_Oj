c = 0
while True:
    try:
        s = str(input()).lower()
        c += s.count("m")
    except EOFError:
        break
print(c)
