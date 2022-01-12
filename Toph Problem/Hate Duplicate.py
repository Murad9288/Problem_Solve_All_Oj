for _ in range(int(input())):
    s = str(input())
    mylist = list(s)
    mylist = list(dict.fromkeys(mylist))
    c = ""
    for i in mylist:
        c += i
    print(c)
