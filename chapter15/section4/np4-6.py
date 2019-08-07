import numpy as np
data = np.array([1,2,3])
print(data.repeat(3))   #各要素を３回ずつ繰り返している

print(data.repeat(3).reshape(3,3))  #各行の値が同じ配列を作る

data = np.arange(6).reshape(2,3)
print(data)
print(data.repeat(2, axis=0))   #行を2回繰り返す
print(data.repeat(2, axis=1))   #列を2回繰り返す
