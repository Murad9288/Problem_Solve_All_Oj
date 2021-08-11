def swap_case(s):
    a = list(s)
    b = []
    for i in a:
        if i.islower():
             b.append(i.upper())
        else:
            b.append(i.lower())
    return("".join(b))
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
