import numpy as np

# np.where(condition, value_if_true, value_if_false)
arr = np.array([-3, -1, 0, 2, 4])
arr0 = np.where(arr < 0, 0, arr )
print(arr0)
arr1 = np.where(arr < 0, 0.01 * arr, arr)
print(arr1)  # leaky relu
arr2 = np.where(arr < 0)
print(arr2)  # returns indices where condition is True

# np.linspace(start, stop, num=50, endpoint=True(def), retstep=False, dtype=None)
arr3 = np.linspace(1, 10, 5)
print(arr3)
arr4 = np.linspace(1, 10, 5, endpoint=False)
print(arr4)
arr5, step = np.linspace(1, 10, 5, retstep=True)
print("Array: ", arr5)
print("Step size: ", step)
arr6, step0 = np.linspace(5, 50, 10, endpoint=False, retstep=True)
print("Array: ", arr6)
print("Step size: ", step0)

# np.arange(start, stop, step, dtype=None)
arr7 = np.arange(10)
print(arr7)
arr8 = np.arange(1, 10, 2)
print(arr8)
arr9 = np.arange(0, 5, 0.5)
print(arr9)
arr10 = np.arange(5, 50, 5)
print(arr10)
arr11 = np.array([10, 15, 20, 25, 30, 35, 40, 45, 50])
arr12 = np.arange(0, len(arr11), 3)
arr13 = arr11[arr12]
print(arr13)