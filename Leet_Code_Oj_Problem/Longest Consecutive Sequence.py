class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        c = 0
        s = set(nums)
        for i in s:
            if i-1 in s:
                continue
            m = 1
            while i+1 in s:
                m += 1
                i += 1
            c = max(c, m)
        return c
