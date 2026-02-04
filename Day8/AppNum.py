#pip install numpy

import numpy as np
arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
for x in arr:
    print(x)
print("...")
reshapedArr = arr.reshape(4,3)
# print(reshapedArr)
# 1,2,3
# 4,5,6
# 7,8,9
# 10,11,12
for subArr in reshapedArr:
    for y in subArr:
        print(y)
reshapedArr3x4 = arr.reshape(3,4)
# print(reshapedArr3x4)
reshapedArr3d = arr.reshape(2,3,2)
# print("...")
# print(reshapedArr3d)
# newArr = arr.copy()
# newArr[3]= 25
# newView = arr.view()
# print(f"copy {newArr}")
# print(f"orig array:{arr}")
# newView[4] = 36
# print(f"(after view modification) orig array:{arr}")
# print(f"shape of array: {arr.shape}")
# arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
# print("shape:", arr.shape)
