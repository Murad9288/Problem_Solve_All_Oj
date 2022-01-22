def fibo(n):
    if n==0 or n==1:
        return "IsFibo"

    f1=f2=1
    while n>f2:
        f1, f2 = f1+f2, f1+f2+f2
        if n==f1 or n==f2:
            return "IsFibo"

    return "IsNotFibo"
if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        print(fibo(n))
