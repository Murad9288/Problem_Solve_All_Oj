T = int(input())
for i in range(1,T+1):
    string = input()
    character = input()
    if character in string:
        print("Occurrence of '%s' in '%s' ="%(character,string),string.count(character))
    else:
        print("'%s' is not present"%character)
