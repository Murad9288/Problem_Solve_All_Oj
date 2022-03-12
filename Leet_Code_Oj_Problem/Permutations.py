from itertools import permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        arr = list(permutations(nums,len(nums)))
        return arr
