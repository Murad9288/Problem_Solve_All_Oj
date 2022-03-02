for t in range(int(input())):
    o = 0
    e = 0
    for _ in range(int(input())):
        n = int(input())
        if n%2 == 0:
            e += 1
        else:
            o += 1
    if o>e:
        print("For student %d :- Friendship Accepted."%(t+1))
    elif o<e:
        print("For student %d :- Friendship not possible."%(t+1))
    else:
        print("For student %d :- I am confused."%(t+1))
