class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        n = len(nums)
        result = +2147483647
        # Sorting the array.
        nums.sort()

        # Find minimum value among
        # all K size subarray.
        for i in range(n-k+1):
            result = int(min(result, nums[i+k-1] -nums[i]))

        return result

# Second Rules:
'''
# Python program to find minimum
# difference of maximum
# and minimum of K number.
 
# Return minimum difference
# of maximum and minimum
# of k elements of arr[0..n-1].
def minDiff(arr,n,k):
    result = +2147483647

    # Sorting the array.
    arr.sort()

    # Find minimum value among
    # all K size subarray.
    for i in range(n-k+1):
        result = int(min(result, arr[i+k-1] - arr[i]))

    return result

# Driver code

arr= list(map(int,input().split()))
n =len(arr)
k = int(input())

print(minDiff(arr, n, k))
'''
