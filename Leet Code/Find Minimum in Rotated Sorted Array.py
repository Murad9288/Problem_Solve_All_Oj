class Solution:
    def findMin(self, nums: List[int]) -> int:
        L = sorted(nums)
        return(min(L))
