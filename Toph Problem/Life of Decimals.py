for _ in range(int(input())):
    n = int(input())
    a = [1,4,1,5,9,2,6,5,3,5,8,9]
    if n == 1 or n == 3:
        print(1)
    elif n == 2:
        print(4)
    elif n == 4 or n == 8 or n == 10:
        print(5)
    elif n == 5 or n == 12:
        print(9)
    elif n == 6:
        print(2)
    elif n == 7:
        print(6)
    elif n == 9:
        print(3)
    elif n == 11:
        print(8)
    else:
        print("Wrong!")

# Second System:
'''
for _ in range(int(input())):
    n = int(input())
    a = [1,4,1,5,9,2,6,5,3,5,8,9]
    for i in a:
        print(a[n-1])
        break
'''
