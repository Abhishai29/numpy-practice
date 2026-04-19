import numpy as np

# create 1D, 2D, 3D arrays
arr1 = np.array([1,2,3,4,5,6])
print(arr1)   # 1D array
print(arr1.reshape(2,3))   # 1D ---> 2D
print(arr1.reshape(2,1,3))   # 1D ---> 3D

arr2 = np.array([[1,2],[3,4]])  
print(arr2)   # 2D array
print(arr2.reshape(-1))    # 2D ---> 1D

arr3 = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(arr3)   # 3D array
print(arr3.reshape(-1))    # 3D ---> 1D

arr4 = np.array([1,2,3,4,5,6,7,8])
print(arr4.reshape(4,-1))    # dynamic reshaping

arr5 = np.array([1,2,3,4,5,6])
print(arr5.reshape(2,3))    # row-wise (C-style order)
print(arr5.reshape(2,3, order = 'F'))   # column-wise (Fortan order)

print(np.ravel(arr3))   # flatten to 1D
