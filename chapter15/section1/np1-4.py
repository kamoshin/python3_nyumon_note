import numpy as np
a = np.array([[0,1],[2,3],[4,5]])
print(a)
print(np.transpose(a))  #transposeで転置する
print(a.T)              #Tで転置する（結果は同じ）
