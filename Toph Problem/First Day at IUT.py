for _ in range(int(input())):
    s,n = map(str,input().split())
    y = n[0:2]
    d2 = n[4:6]
    sec = n[6:7]
    a = ""
    for i in d2:
        a += i
    d = int(a)
    if d == 11 or d == 12:
        print("Name: %s"%s)
        print("Student id: %s"%n)
        print("Batch: 20%s"%y)
        print("Department: MPE")
        print("Section: %s"%sec)

    elif d == 21:
        print("Name: %s"%s)
        print("Student id: %s"%n)
        print("Batch: 20%s"%y)
        print("Department: EEE")
        print("Section: %s"%sec)
    elif d == 31:
        print("Name: %s"%s)
        print("Student id: %s"%n)
        print("Batch: 20%s"%y)
        print("Department: TVE")
        print("Section: %s"%sec)

    elif d == 41 or d == 42:
        print("Name: %s"%s)
        print("Student id: %s"%n)
        print("Batch: 20%s"%y)
        print("Department: CSE")
        print("Section: %s"%sec)

    elif d == 51:
        print("Name: %s"%s)
        print("Student id: %s"%n)
        print("Batch: 20%s"%y)
        print("Department: CEE")
        print("Section: %s"%sec)
    elif d == 61:
        print("Name: %s"%s)
        print("Student id: %s"%n)
        print("Batch: 20%s"%y)
        print("Department: BTM")
        print("Section: %s"%sec)




