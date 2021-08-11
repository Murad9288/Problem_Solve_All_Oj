import math
def simplePrimaryTest(number):
    if number == 1:
        return "Not prime"
    if number == 2:
       return "Prime"
    if number % 2 == 0:
        return "Not prime"

    i = 3
    sqrtOfNumber = math.sqrt(number)

    while i <= sqrtOfNumber:
        if number % i == 0:
            return "Not prime"
        i = i+2

    return "Prime"
for _ in range(int(input())):
    number = int(input().strip())
    print(simplePrimaryTest(number))
