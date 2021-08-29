if __name__ =='__main__':
    n  = int(input())
    for i in range(n):
        s = input().strip()
        result= sorted(list(set(s)))
        for x in result:
            c = s.count(x)
            print("%c = %d"%(x,c))
        if i < n-1:
            print()
