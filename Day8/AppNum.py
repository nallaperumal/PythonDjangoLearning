#pip install numpy

import numpy as np

arr1  =np.array( [[1,2],[3,4]])
arr2  =np.array( [[4,5],[6,7]])

mulArr = arr1 @ arr2
print(mulArr)
arr1 = np.random.randint(0, 9, size = (3,3))
print(arr1)
np.savetxt('mat1.csv', arr1, delimiter=',', header="id,mark,rank", footer="@2026", fmt="%d")

retreivedMat = np.genfromtxt('mat1.csv',delimiter=",")
print(retreivedMat)
# joinedArr = np.concatenate((arr1, arr2))
# print(joinedArr)
# splittedArr = np.array_split(joinedArr,2)
# print(splittedArr)
# joinedArr = np.vstack((arr1, arr2))
# print(joinedArr)
# print(np.average(joinedArr))
# print(np.sum(joinedArr))
# print(np.sqrt(joinedArr))

# arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# for x in arr:
#     print(x)
# print("...")
# reshapedArr = arr.reshape(4,3)
# for subArr in reshapedArr:
#     for y in subArr:
#         print(y)
# reshapedArr3x4 = arr.reshape(3,4)
# reshapedArr3d = arr.reshape(2,3,2)
