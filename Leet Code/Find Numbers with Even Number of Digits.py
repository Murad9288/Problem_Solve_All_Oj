class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        sum = 0
        for i in nums:
            if  100>i>=10:
                sum += 1
            elif 10000>i>=1000:
                sum += 1
            elif i == 100000:
                sum += 1
        return(sum)
