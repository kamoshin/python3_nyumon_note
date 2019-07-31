import numpy as np
a = np.array([[1,2,3], [4,5,6]])
print(a)

line1 = [10,20,30]
line2 = [40,50,60]
line3 = [70,80,90]
a = np.array([line1, line2, line3])
print(a)

data = [1,2,3,4,5,6]
a = np.array(data)
print(a)
a = a.reshape(2, 3)
print(a)

a = np.array([[0,1], [2,3], [4,5]])
print(a.ravel())
print(a.flatten())

a = np.array([[0,1],[2,3],[4,5]])
print(a.shape)
print(a.ndim)
print(a.size)

