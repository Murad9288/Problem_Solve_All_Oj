T = int(input())
for i in range(T):
    s = str(input())
    L = s.lower()
    count = 0
    li = ['a','e','i','o','u']
    for i in L:
        if i in li:
            count = count + 1
    print("Number of vowels =",count)
