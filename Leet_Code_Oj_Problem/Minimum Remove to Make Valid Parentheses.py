class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        count = s.count(")")
        c = 0
        string = ""
        for i in s:
            if i == '(':
                c += 1
                if c <= count: 
                    string += '('
            elif i == ')':
                if c > 0: 
                    string += ')'
                count -= 1
                c -= 1
                if c < 0: 
                    c = 0
            else: 
                string += i
        return string
