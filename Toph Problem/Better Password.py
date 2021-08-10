# Simple input:
'''
unsophisticated
'''
# Simple output:
'''
Un$()ph!$t!cated.
'''

string = input()
capital = str(string).capitalize()
list = []
for i in capital:
    if i == "s":
        i = "$"
    if i == "i":
        i = "!"
    if i == "o":
        i = "()"
    list.append(i)
for j in list:
    print(j, end="")
print(".")
