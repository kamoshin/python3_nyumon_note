import numpy as np
data = np.array([10,20,30,40,50,60]).reshape(2,3)
for i, item in np.ndenumerate(data):    #多次元配列から位置と要素を取り出す
    print(i, item)      #iには(行、列)のタプルが入る