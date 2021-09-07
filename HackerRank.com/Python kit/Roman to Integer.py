s = str(input())
roman = {'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5,'VI': 6, 'VII': 7, 'VIII': 8, 'IX': 9, 'X': 10,'XL': 40, 'L': 50,
         'XC': 90, 'C': 100,'CD': 400, 'D': 500,'CM': 900, 'M': 1000}

if s in roman:
    print(roman[s])
else:
    result = 0
    i = 0
    string = ""
    while i < len(s):
        last = string
        string += s[i]
        if string in roman:
            if (i == len(s) - 1):
                result += roman[string]
            i += 1
        else:
            result += roman[last]
            string = ""
    print(result)
