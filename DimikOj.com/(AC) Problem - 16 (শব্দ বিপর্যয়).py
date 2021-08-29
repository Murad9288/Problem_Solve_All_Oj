test = int(input())
for i in range(test):
    sentence = input().split(' ')
    res = []
    for x in sentence:
        word = "".join(x[::-1]) # eikhane word = "".join(reversed(x)) likhlew hobe..
        res.append(word)
    print(' '.join(res))
