import numpy as np
#多重リストから2行3列の配列を作る
a = np.array([[1,2,3], [4,5,6]])    #2次元リストの配列を作る
print(a)        #2行3列の配列ができる

#3行3列の配列を作る
line1 = [10,20,30]
line2 = [40,50,60]
line3 = [70,80,90]
a = np.array([line1, line2, line3]) #3個のリストから配列を作る
print(a)        #3行3列の配列ができる

#1次元配列を2行3列の配列に変換する
data = [1,2,3,4,5,6]
a = np.array(data)
print(a)
a = a.reshape(2, 3)     #2行3列の配列にする
print(a)

#多次元配列を1次元配列にする
a = np.array([[0,1], [2,3], [4,5]])
print(a.ravel())        #１次元配列になる
print(a.flatten())      #新しくメモリを確保して1次元配列にする

#配列の構造を調べる
a = np.array([[0,1],[2,3],[4,5]])
print(a.shape)  #３行２列
print(a.ndim)   #２次元配列
print(a.size)   #要素の個数

