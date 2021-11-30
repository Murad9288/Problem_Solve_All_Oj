class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for _ in range(len(nums)):
            if nums[0] != val:
                nums.append(nums[0])
            nums.pop(0)
        return len(nums)
