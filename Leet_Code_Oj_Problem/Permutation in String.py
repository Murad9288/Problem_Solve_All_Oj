class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        a = Counter(s1)
        b = len(s1)
        
        for i in range(len(s2)-len(s1)+1):
            c = Counter(s2[i:i+b])
            if a==c:
                return True
        return False
