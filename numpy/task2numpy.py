import numpy as np
# array indexing and slicing
arr = np.array([[10,20,30],[40,50,60]])
print(arr[1,1])    # extract 50
print(arr[1,-2])    # extract 50  (-ve indexing)
print(arr[0,:])    # extract 1st row
print(arr[:,1])    # extract 2nd column

# stacking arrays
a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])

print(np.vstack((a,b)))   # vertical
print(np.hstack((a,b)))   # horizontal

# extract elements based on condition
arr1 = np.array([10,20,30,40,50,60])

print(arr1[arr1>20])     # values > 20
arr1[arr1 > 25] = 100     # replace value
print(arr1)
arr2 = np.array([10,25,30,40,55,60])
print(arr2[arr2 % 2 == 0])