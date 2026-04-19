import numpy as np

# creating arrays
arr1 = np.array([1,2,3,4])
print(arr1)     # 1D Array (Vector)

arr2 = np.array([[1,2,3],[4,5,6]])
print(arr2)     # 2D Array (Matrix)

# random number generation
arr3 = np.random.rand(3,3)
print(arr3)     # 3x3 matrix with values btw 0 & 1

arr4 = np.random.randint(1,10,(2,3))
print(arr4)     # 2x3 matrix with nos. from 1 to 9

arr5 = np.random.randn(4)  # mean = 0, std = 1
print(arr5)     # 4 random numbers from normal distribution

arr0 = np.random.uniform

# numpy array operations
a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])
print(a + b)    # addition
print(a * b)    # multiplication
print(a ** 2)    # squares each element
print(np.dot(a,b))     # matrix multiplication

# useful numpy functions
arr6 = np.array([1,2,3,4,5])
print(np.sum(arr6))
print(np.mean(arr6))
print(np.max(arr6))
print(np.min(arr6))
print(np.median(arr6))
print(np.std(arr6))

# axis = 0 : operate column-wise (down)
# axis = 1 : operate row-wise (across)
# keepdims = True : Maintains original dimensions

