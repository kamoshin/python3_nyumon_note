import numpy as np
#ベクトルaを行列Aで表す
p0 = np.array((1,1))    #点p0の座標
p1 = np.array((6,4))    #点p1の座標
A = p1 - p0     #ベクトルaを示す配列
print(A)

#ベクトルaの長さ
a_norm = np.linalg.norm(A)  #ベクトルの長さを求める
print(a_norm)

#ベクトルaの2倍の長さのベクトル
A2 = A*2        #ベクトルaの長さを２倍にする
a2_norm = np.linalg.norm(A*2)
print(a2_norm)