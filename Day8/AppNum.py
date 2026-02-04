#pip install numpy

import numpy as np
arr = np.array([1,2,3,4])
print(np.__version__)
print(arr)
print(type(arr))
arrT = np.array((1,2,5,6))
print(arrT)
print(type(arrT))
arr2D = np.array([[1,2,3],[2,1,3]])
arr4D = np.array([[[[1,2,3],[2,1,3]]]])
print(arr4D)
print(arr2D.ndim)
print(arr4D.ndim)