
import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    a = (numpy.array(arr, float))[::-1]
    return a

#arr = [1, 2, 3, 4, -8, -10]
arr = input().strip().split(' ')
result = arrays(arr)
print(result)

# Success!