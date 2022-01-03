class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a = s.strip().split(" ")
        return(len(a[-1]))
