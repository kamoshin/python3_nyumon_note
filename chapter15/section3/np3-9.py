import numpy as np
A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])
C = np.dot(A, B)    #行列A、Bの内積
print(C)

#仕事を内積dot()で計算する
F = np.array([8.66, 5.0])   #ベクトルF
S = np.array([20, 0])   #ベクトルS
W = np.dot(F, S)    #仕事(内積)を求める
print(W)

#dot()の結果を検算する
#仕事 ＝ 距離 × 力 = |S||F|cos(θ)
f = np.linalg.norm(F)   #ベクトルFの長さ
s = np.linalg.norm(S)   #ベクトルSの長さ
rad = np.radians(30)    #３０度をラジアンに換算
w = f * s * np.cos(rad) #仕事を計算
print(w)

#３次元ベクトルa、bの外積となるベクトルcを求める
#面積S = |a||b|sinθ
a = np.array([1,2,0])
b = np.array([0,1,-1])
c = np.cross(a,b)   #外積
print(c)