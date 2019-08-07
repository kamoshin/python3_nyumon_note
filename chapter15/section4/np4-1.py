import numpy as np
print(np.arange(10))

n = 3
m = 4
print(np.arange(n*m).reshape(n,m))  #0~11の数値から３行４列の配列を作る

print(np.arange(10,20,2))   #10から2ずつ増える

print(np.arange(10, step = 0.5))

A = np.array([1,2,3,4,5,6]).reshape(2,3)
B = np.array([1,2,9,4,8,6]).reshape(2,3)
C = (A == B)    #AとBを比較した結果の配列Cを作る
print(C)        #A、Bの要素を比較し、同じ位置はTrue、異なる位置にはFalseが入る

n = (A != B).sum()  #要素が異なる数を数える
print(n)