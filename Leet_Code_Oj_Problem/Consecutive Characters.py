class Solution:
    def maxPower(self, s: str) -> int:
        c = 1
        res = 1
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                c += 1
                res = max(c,res)
            else:
                c = 1
        return res


# Simple code solution.
'''
s = str(input())
c = 1
res = 1
for i in range(len(s)-1):
    if s[i] == s[i+1]:
        c += 1
        res = max(c,res)
    else:
        c = 1
print(res)

'''
