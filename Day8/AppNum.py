#pip install numpy

import numpy as np
arr = np.array([1,2,3,4,5,6,7])
newArr = arr.copy()
newArr[3]= 25
newView = arr.view()
print(f"copy {newArr}")
print(f"orig array:{arr}")
newView[4] = 36
print(f"(after view modification) orig array:{arr}")
print(f"shape of array: {arr.shape}")
# print(arr[0])
# print(arr[1])
# print(arr[1:])
# print(arr[:2])
# print(arr[::2])
# print(arr[1::2]) #arr[<startIndex>:<EndIndex>:<steps>]
arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print("shape:", arr.shape)
# print(arr[1][3])
# print(arr[1, 1:4])
# print(arr[0, 3:5])