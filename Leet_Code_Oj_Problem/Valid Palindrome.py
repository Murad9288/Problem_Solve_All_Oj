class Solution(object):
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        palindrome = ""

        for i in range(len(s)):
            if(s[i].isalnum()):
                palindrome+=s[i]

        j = len(palindrome)-1
        for i in range(len(palindrome)):
            if(palindrome[i]!=palindrome[j]):
                return False
            j-=1
        return True
