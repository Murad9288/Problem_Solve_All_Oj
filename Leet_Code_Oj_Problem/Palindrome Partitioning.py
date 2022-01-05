class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ret = []
        def solve(s):
            return s == s[::-1]
        
        def answer(s, l):
            if not s:
                ret.append(l)
                return
            for i in range(1, len(s)+1):
                if solve(s[:i]):
                    answer(s[i:], l+[s[:i]])
        answer(s, [])
        return ret
