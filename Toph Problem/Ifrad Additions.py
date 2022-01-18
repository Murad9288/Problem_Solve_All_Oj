number1,number2 = map(int,input().split())
l = len(str(number1))
l1 = len(str(number2))
def carries():
    num1 = str(number1)
    num2 = str(number2)
    carry = 0
    carries = 0
    c1 = l
    c2 = l
    if (l < l1):
        while (c1 < l1):
            num1 = '0' + num1
            c1+=1
    if (l1 < l):
        while (c2 < l):
            num2 = '0' + num2
            c2+=1
    i = c1
    while (i > 0):
        if (int(num1[i-1])+int(num2[i-1])+carry > 9):
            carry = 1
            carries+=1
        else:
            carry = 0
        i-=1
    return carries
if carries() > 0:
    print("Yes")
else:
    print("No")
