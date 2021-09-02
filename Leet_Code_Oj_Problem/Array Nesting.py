class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        n = len(nums)
        nes = [0]*n
        for i in range(n):
            start, depth = i, 1
            while not nes[start]:
                nes[start] = depth
                start = nums[start]
                depth += 1
                
        return max(nes) 
