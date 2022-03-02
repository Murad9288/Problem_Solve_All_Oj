import numpy

def arrays(arr):
    return numpy.array(arr, float)[::-1]

arr = raw_input().strip().split(' ')
result = arrays(arr)
print(result)
