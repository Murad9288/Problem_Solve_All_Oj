n = int(input())
book = {}

for i in range(n):
    li = list(map(str,input().split()))
    key = li[0]
    value = li[1]
    book[key] = value
while True:
    try:
        name = input()
        if name in book:
            print(name + "=" + book[name])
        else:
            print("Not found")
    except:
        break
