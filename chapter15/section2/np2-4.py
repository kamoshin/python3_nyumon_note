import numpy as np
data = np.array([10,20,30,40,50,60]).reshape(2,3)
for i, item in np.ndenumerate(data):
    print(i, item)