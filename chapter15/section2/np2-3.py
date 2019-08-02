import numpy as np
#多次元配列のスライス
data = [10,20,30,40,50,60,70,80,90]
a = np.array(data).reshape(3,3)
print(a)
print(a[:2,])       #０～１行目、すべての列
print(a[:,1:])      #全ての行、１列目以降
print(a[1:,1:])     #１行目以降、１列目以降

#スライスと同時に型変換する
data = [2.1, 3.5, 2.5, 4.3, 5.1, 1.6]
a = np.array(data).reshape(3,2)
print(a)
a2 = a[:2,].astype(int)     #最初の２行を取り出す際に整数に変換する
print(a2)       #値が整数に変換されている