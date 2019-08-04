import numpy as np
A = np.array([10,20,30,40]).reshape(2,2)
print(A)
B = A + 5       #配列のすべての要素に５を足す
print(B)
print(A - 5)    #配列のすべての要素から５を引く
print(A * 5)    #配列のすべての要素に５を掛ける
print(A / 5)    #配列のすべての要素を２で割る
