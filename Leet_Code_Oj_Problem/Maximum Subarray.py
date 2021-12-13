class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s = sum(nums)
        c = 0
        for i in nums:
            if c < 0:
                c = i
            else:
                c += i
            s = max(s,c)
        return s
