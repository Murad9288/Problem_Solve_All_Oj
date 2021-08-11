# Only two test case not accepted.


import sys
sys.setrecursionlimit(10**6)

def soln(arr):
    if len(arr)<=1:
        return 0
    
    # to get index of max value
    indx=arr.index(max(arr))
    
    # splitting and recurssion -> (d & c) -> (MemoryError)
    x= soln(arr[0:indx+1] if indx != len(arr)-1 else arr[0:indx]) + soln(arr[indx+1:])
    
    # sorting operation
    arr=sorted(arr[0:indx+1])+sorted(arr[indx+1:])
    
    # indexes for while loop
    i=indx-1 if indx == len(arr)-1 else indx
    j=indx+1 if indx !=len(arr)-1 else indx
    
    # logic for pair count
    while i>=0 and j<len(arr):
        p=arr[i]*arr[j]
        if p <= arr[indx]:
            x+=i+1
            j+=1
        else:
            i-=1
            
    # recurrsion
    return x

# .......................Input-Output-Section.........................
# Input by user
n=int(input())
arr=list(map(int, input().split()))

# Uncomment below statements for MemoryError inputs

# MemoryError input 1
# arr=[2 if i%2==1 else 1 for i in range(1, 500001)]

# MemoryError input 2
# arr=[100000 for i in range(100000)]

print(soln(arr))
