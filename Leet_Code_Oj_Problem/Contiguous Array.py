class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        s = {}
        sum = 0
        c = 0
        k = 0
        for i,j in enumerate(nums):  
            if j == 0:
                j = -1
            sum += j
            if sum not in s:
                s[sum] = i
            if sum == k:
                c = max(c, i+1)
            if sum-k in s:
                c = max(c, i - s[sum-k])
        return c
