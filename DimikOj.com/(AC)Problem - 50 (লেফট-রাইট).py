for _ in range(int(input())):
    S = list(input())
    for index in range (len(S)):
        if S[index] == 'L':
            S[index] = S[index-1]
        elif S[index] == 'R':
            S[index] = S[index+1]
        else:
            S[index] = S[index]
    print(''.join(S))
