try:
     x = int(input()) - 1
     arr = list(map(int, input().split()))
     a = 1
     while True:
         c = 0
         for i in arr:
             if i % a == 0:
                 c += 1
         if c == x:
             print(a)
             break
         a += 1
e
