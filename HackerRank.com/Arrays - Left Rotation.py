def left_shift(n,k,a):
   for _ in range(k):
      a.append(a.pop(0))
   print(*a)

if __name__ == '__main__':

    n, k = map(int,input().strip().split())
    a = list(map(int,input().strip().split()))
    left_shift(n,k,a)
    
