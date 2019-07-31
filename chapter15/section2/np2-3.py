import numpy as np
data = [10,20,30,40,50,60,70,80,90]
a = np.array(data).reshape(3,3)
print(a)
print(a[:2,])
print(a[:,1:])
print(a[1:,1:])

data = [2.1, 3.5, 2.5, 4.3, 5.1, 1.6]
a = np.array(data).reshape(3,2)
print(a)
a2 = a[:2,].astype(int)
print(a2)