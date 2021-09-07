for _ in range(int(input())):
    count = 0
    word = input()
    for i in range(len(word) - 1):
        if word[i] == word[i + 1]:
            count += 1
    print(count)    
