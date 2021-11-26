for _ in range(int(input())):
    n = str(input())
    l = list(n)
    r = l[:-1]
    last = l[-1]
    l_2 = l[1:]
    first = l[0]
    res_1 = r[::-1]
    res_2 = l_2[::-1]
    string = ""
    string_2 = ""
    for i in res_1:
        string += "".join(str(i))
    for j in last:
        string += "".join(str(j))
    for i in res_2:
        string_2 += "".join(str(i))
    for j in first:
        string_2 += "".join(str(j))
    print(string[::-1])
    print(string_2[::-1])
