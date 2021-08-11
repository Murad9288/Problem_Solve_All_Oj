# eita function chara hoyeche....
s = input()
for x in s[:].split():
    s = s.replace(x, x.capitalize())
print(s)


# Function diye korano hoyeche.,.
'''def solve(s):
    s = s.split(" ")
    return(" ".join(i.capitalize() for i in s))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()'''
