import numpy as np
a = np.array([1,2,3,4,5,6,7,8,9])
print(a[a>=5])
print(a[a%2 == 0])
print(a[a%2 == 1])

b = a.reshape(3,3)
print(b[b>5])
print(a[(a>=5) & (a%2 == 1)])
print(a[(a%2 == 0) | (a%3 == 0)])
print(a[~(a%3 == 0)])
