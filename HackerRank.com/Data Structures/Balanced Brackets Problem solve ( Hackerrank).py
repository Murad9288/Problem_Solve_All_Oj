# Simple Input:
'''
6
}][}}(}][))]
[](){()}
()
({}([][]))[]()
{)[](}]}]}))}(())(
([[)
'''
# Output:
'''
NO
YES
YES
YES
NO
NO
'''
def Balanced_Brkt(string):
    Stack = []
    st = {")": "(","}": "{","]": "["}
    for result in string:
        if not Stack:
            Stack.append(result)
        elif result not in st:
            Stack.append(result)
        elif st[result] == Stack[-1]:
            Stack.pop()
        else:
            Stack.append(result)
    if Stack:
        print("NO")
    else:
        print("YES")

N = int(input().strip())
for i in range(N):
     string = input()
     Balanced_Brkt(string)

# fucntion baad diye
'''
N = int(input().strip())
for i in range(N):
     string = input()
     Stack = []
     st = {")": "(","}": "{","]": "["}
     for result in string:
         if not Stack:
             Stack.append(result)
         elif result not in st:
             Stack.append(result)
         elif st[result] == Stack[-1]:
             Stack.pop()
         else:
             Stack.append(result)
     if Stack:
         print("NO")
     else:
         print("YES")
'''
