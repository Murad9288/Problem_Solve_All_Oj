n = int(input())
if n>1:
    if (n+1)%6 == 0 or (n-1)%6 == 0 or n == 2 or n == 3:
        print("NO PUNISHMENT")
    else:
        for i in range(n):
            print("I DID NOT DO THE ASSIGNMENT.")
else:
    for i in range(n):
        print("I DID NOT DO THE ASSIGNMENT.")
