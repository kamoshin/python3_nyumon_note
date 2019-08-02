import numpy as np
a = np.array([1,2,3,4,5,6,7,8,9])
print(a[a>=5])      #５以上の値を抽出
print(a[a%2 == 0])  #偶数
print(a[a%2 == 1])  #奇数

#論理演算式を利用する
b = a.reshape(3,3)
print(b[b>5])   #多次元配列から５より大きい値
print(a[(a>=5) & (a%2 == 1)])       #論理積(５以上かつ奇数)
print(a[(a%2 == 0) | (a%3 == 0)])   #論理和(２または３の倍数)
print(a[~(a%3 == 0)])   #論理否定(３の倍数ではない)
