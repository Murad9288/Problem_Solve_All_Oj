class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            if nums[i + 1: i + 3].count(nums[i]) == 2:
                nums.pop(i)
            else:
                i += 1
