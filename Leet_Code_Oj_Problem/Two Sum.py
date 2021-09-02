class Solution:
    def twoSum(self, n:List[int], t:int) -> List[int]:
        x = len(n)
        for i in range(x-1):
            for j in range(i+1, x):
                if n[i] + n[j] == t:
                    return [i, j]
