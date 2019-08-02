import numpy as np
a = np.array([3,1,6,3,7,2,9,6,5,2,1,7,8,3,1,3])
a = a.reshape(4,4)
print(a)
a[a%2 == 0] = 0     #偶数を０に置き換える
print(a)
a[a%2 == 1] = 1     #奇数を１に置き換える
print(a)
