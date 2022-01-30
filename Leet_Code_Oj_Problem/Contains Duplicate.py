class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        s = len(set(nums))
        if n>s:
            return True
        else:
            return False
        
