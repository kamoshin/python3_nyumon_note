import numpy as np
A = np.array([1,2,3,4]).reshape(2,2)    #２行２列の配列
print(A)
B = np.array([100, 200])        #１行１列の配列
print(B)
C = A + B       #行数が足りない配列を足す
print(C)

A = np.array([1,2,3,4,5,6]).reshape(2,3)    #２行３列の配列
print(A)
B = np.array([10,20]).reshape(2,1)      #２行１列の配列
print(B)
C = A + B       #列数が足りない配列を足す
print(C)
