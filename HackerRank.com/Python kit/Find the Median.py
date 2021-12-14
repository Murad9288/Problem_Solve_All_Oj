# First System:
'''
# Import statistics Library
import statistics

# Calculate middle values
n = int(input())
arr = list(map(int,input().split())) [:n]
print(statistics.median(arr))

'''

# Second System:
# Not user define function use:

n = int(input())
arr = list(map(int,input().split())) [:n]
s = sorted(arr)
if n%2 == 0:
    m1 = n/2
    m2 = (n/2)+1
    m1 = int(m1) - 1 # -1 is given to find out as an index.
    m2 = int(m2) - 1 # i-1 is given to find out as an index.
    mid = (arr[m1]+arr[m2]) / 2
else:
    m = (n+1)/2
    m = int(m) - 1 # -1 is given to find out as an index.
    mid = arr[m]
print(mid)



# Third System:
# use to user define function:

'''
def calculate_median(arr):
    N = len(arr)
    arr.sort()

    #find the median
    if N % 2 == 0:
        #if N is even
        m1 = N / 2
        m2 = (N / 2) + 1
        #Convert to integer, match post
        m1 = int(m1) - 1
        m2 = int(m2) - 1
        median = (arr[m1] + arr[m2]) / 2
    else:
        m = (N + 1) / 2
        # Convert to integer, match position
        m = int(m) - 1
        median = arr[m]

    return median
  
n = int(input())
arr = list(map(int,input().split())) [:n]
print(calculate_median(arr))
'''
