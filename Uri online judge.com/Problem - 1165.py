for _ in range(int(input())):
    n = int(input())
#   ans = False
    if n>1:
        for i in range(2,n):
            if n%i == 0:
                print("%d nao eh primo"%n)
            #   ans = True
                break
        else:
            print("%d eh primo"%n)
    else:
        print("%d nao eh primo"%n)

    '''if ans:
        print("%d nao eh primo"%n)
    else:
        print("%d eh primo"%n)'''
