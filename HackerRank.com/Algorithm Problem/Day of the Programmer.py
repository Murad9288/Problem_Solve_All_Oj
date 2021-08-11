n = int(input())
if n == 1918:
    print("26.09.1918")
elif n%4 == 0 and (n<1918 or n%400==0 or n%100 != 0):
    print("12.09.%d"%n)
else:
    print("13.09.%d"%n)
