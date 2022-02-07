for _ in range(int(input())):
    s = str(input())
    b = ""
    for i in s:
        if i == "n" or i == "e" or i == "p" or i == "a" or i == "l":
            b += i
    if len(set(b)) == 5:
        print("Maile Nepal banauna sakchhu!!")
    else:
        print("Hami sabai milera Nepal Banau hai!!")
