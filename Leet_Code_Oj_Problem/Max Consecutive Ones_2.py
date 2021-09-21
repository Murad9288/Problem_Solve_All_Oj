class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res, count, l_n = 0, 0, -1
        for i in nums:
            if l_n != i:
                l_n = i
                count = 1
            else:
                count += 1
            if i == 1:
                res = max(res, count)
        return res
'''
my_class = Solution()
nums = list(map(int,input().split()))
print(my_class.findMaxConsecutiveOnes(nums))


'''
