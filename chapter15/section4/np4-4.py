import numpy as np
E = np.identity(4)  #４行４列の単位行列を作る
print(E)

E = np.eye(3)   #eye()を使って単位行列を作る
print(E)

E = np.identity(3, dtype=int)   #整数値の単位行列を作る
print(E)