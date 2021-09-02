class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        L = []
        for i in nums:
            if i >= 0:
                L.append(i*i)
            else:
                L.append(abs(i*i))
        return(sorted(L))
