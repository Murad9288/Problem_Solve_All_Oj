class Solution:
    def isPalindrome(self, x: int) -> bool:
        L = str(x)
        if L == L[::-1]:
            return True
        else:
            return False
