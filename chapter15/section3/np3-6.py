import numpy as np
A = np.array([1,2,3,4]).reshape(2,2)
print(A)
B = np.array([10,20,30,40]).reshape(2,2)
print(B)
C = A + B   #同じ行列数の配列の足し算
print(C)
D = A * B   #要素同士の掛け算
print(D)
E = A / B   #要素同士の割り算
print(E)