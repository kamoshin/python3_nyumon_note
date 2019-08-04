import numpy as np
A = np.array([52,32,67,84,42,74]).reshape(2,3)
print(A)
print(A.sum())      #全体の合計
print(A.sum(0))     #各列の合計
print(A.sum(1))     #各行の合計

print(A.max())      #全体の最大値
print(A.max(0))     #各列の最大値
print(A.max(1))     #各行の最大値

print(A.min())      #全体の最小値
print(A.min(0))     #各列の最小値
print(A.min(1))     #各行の最小値

print(A.mean())     #全体の平均
print(A.mean(0))    #各列の平均値
print(A.mean(1))    #各行の平均値

#numpyの関数を使う場合の書き方
print(np.sum(A))    #Aの合計値
print(np.max(A,1))  #Aの各行の最大値