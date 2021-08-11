while True:
    n = int(input())
    if n % 2 == 0:
        if n in range(2,6):
            print("Not Weird")

        elif n in range(6,21):
            print("Weird")

        elif n > 20:
            print("Not Weird")
    else:
        print("Weird")
# eikhane duiti code ekrokom...bivinno diye korano hoyeche..
'''if __name__ == '__main__':
  n = int(input())
  print(("Not " if n%2==0 and (n<=4 or n>20) else "") + "Weird")'''
