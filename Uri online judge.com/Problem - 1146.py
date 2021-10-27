while True:
     n = int(input())
     if n == 0:
          break
     else:
          li = []
          for i in range(1,n+1):
               li.append(i)
          print(*li)
