# Sample Input:
'''
4
-1
10
16
18
'''
# Sample Output:
'''
Age is not valid, setting age to 0.
You are young.
You are young.

You are young.
You are a teenager.

You are a teenager.
You are old.

You are old.
You are old.
'''

class Person:
    def __init__(self,initialAge):
        self.age = initialAge
        if self.age < 0:
            self.age = 0
            print("Age is not valid, setting age to 0.")
        else:
            self.initialAge = self.age
            # 0 er kom hole tahole else er khetre amra age value take initialAge valute pathay dibo..

    def amIOld(self):
        if self.age < 13:
            print("You are young.")
        elif self.age > 12 and self.age < 18:
            print("You are a teenager.")
        else:
            print("You are old.")
        # eivabew korano jay..
        '''
        if sel.age in range(0, 13):
            print("You are young.")
        elif self.age in range(13, 18):
            print("You are a teenager.")
        else:
            print("You are young.")
            '''
    def yearPasses(self):
        self.age += 1

t = int(input())
for i in range(0,t):
    age = int(input())
    p = Person(age)
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()
    p.amIOld()
    print("")
