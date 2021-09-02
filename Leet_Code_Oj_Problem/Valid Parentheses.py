class Solution:
    def isValid(self, s: str) -> bool:
        ln = len(s)
        if ln%2 :
            return False
        stack = ['']
        dic = { ')' : '(' , '}':'{' , ']':'[' }
        for c in s :
            if c in ['(' , '[', '{']:
                stack.append(c)
            elif dic[c] != stack[-1] :
                return False
            else :
                stack.pop()
        return stack[-1] == ''
li = Solution()
s = input()
print(li.isValid(s))

# Second rules:
'''
string = input()
length = len(string)
if length%2:
    print(False)

else:
    stack = [""]
    dic = { ")" : "(" , "}":"{" , "]":"[" }
    for c in string:
        if c in ["(","[","{"]:
            stack.append(c)
        elif dic[c] != stack[-1]:
            print(False)
        else:
            stack.pop()
    print(stack[-1] == "")
'''
