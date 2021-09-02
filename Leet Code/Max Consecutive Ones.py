class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result = 0
        local_max = 0
        for i in nums:
            if i:
                local_max += 1
                result = max(result,local_max)
            else:
                local_max = 0
        return(result)
