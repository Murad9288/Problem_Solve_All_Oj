for _ in range(int(input())):
    s = input()
    v = "aeiouAEIOU"
    c = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    vowels = ''
    consonants = ''
    for i in s:
        if i in v:
            vowels += i
        elif i in c:
            consonants += i
    print(vowels)
    print(consonants)
