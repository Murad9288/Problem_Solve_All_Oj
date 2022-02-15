class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]] # Init res set be a empty set
        for i in nums: # Each time add 1 element
            arr = []
            for j in res: # Copy original in res and put num in
                arr.append(j + [i])
            res += arr
        return res
