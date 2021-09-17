if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
maxvalue = -2**31
for i in range(4):
    for j in range(4):
        a = arr[i][j]
        b = arr[i][j+1]
        c = arr[i][j+2]
        d = arr[i+1][j+1]
        e = arr[i+2][j]
        f = arr[i+2][j+1]
        g = arr[i+2][j+2]
        add = a+b+c+d+e+f+g
        if maxvalue<add:
            maxvalue = add
print(maxvalue)
