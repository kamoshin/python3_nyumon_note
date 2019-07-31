import numpy as np
a = np.array([10, 20, 30, 40, 50])
print(a[0])
print(a[1])
print(a[-1])
a[2] = 99
print(a)

data = [10,20,30,40,50,60,70,80,90]
a = np.array(data).reshape(3,3)
print(a[0,0])
print(a[1,1])
print(a[2,-1])

a = np.array([10,20,30,40])
b = a.reshape(2,2)
print(a is b)
b[0,0] = 99
print(b)
print(a)