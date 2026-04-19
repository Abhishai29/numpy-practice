# create a random 4x4 matrix with integers btw 1 & 50 
# extract all elements greater than 20
# compute mean of those elements 
# replace nos. less than 10 with 0
# flatten the matrix into a 1D array

import numpy as np

arr = np.random.randint(1,50,(4,4))
print(arr)    # create a random 4x4 matrix with integers btw 1 & 50 
print(arr[arr > 20])      # extract all elements greater than 20
print(np.mean(arr[arr > 20]))     # compute mean of those elements 
arr[arr < 10] = 0      
print(arr)       # replace nos. less than 10 with 0
print(np.ravel(arr))      # flatten the matrix into a 1D array