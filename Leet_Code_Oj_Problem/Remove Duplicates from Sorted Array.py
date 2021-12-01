class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        temp = 0
        for i in range(1,len(nums)):
            if nums[i] != nums[temp]:
                temp += 1
                nums[temp] = nums[i]
        return temp+1
