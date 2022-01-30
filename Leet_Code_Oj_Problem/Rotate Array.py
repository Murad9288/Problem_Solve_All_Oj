class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums) - k%len(nums)
        nums[:] = nums[n:] + nums[:n]


# myself system:

'''
def array(arr,k):
    res = arr[:k+1]
    res2 = arr[len(res):]
    arr[:] = res2+res
arr = [1,2,3,4,5,6,7]
k = 3
print(array(arr,k))

'''
