for _ in range(int(input())):
     grade = int(input())
     if grade >= 38:
          if grade % 5 == 3:
               grade += 2
          if grade % 5 == 4:
               grade += 1
     print(grade)
