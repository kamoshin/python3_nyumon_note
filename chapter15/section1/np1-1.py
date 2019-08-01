#numpyモジュールにnpの別名をつけてインポートする
import numpy as np

a = np.array([1,2,3])   #リストから配列を作る
data = (1,2,3)
b = np.array(data)      #タプルから配列を作る
print(a,b)          #カンマが取り除かれて出力される
print(type(a))      #配列オブジェクトの型を調べる(ndarrayクラスのメソッドや属性を使える)
print(a.dtype)      #配列の要素の型を調べる

#型が混在している配列は作ることができない
a = np.array([1, 1.5, 2])       #全てfloat型になる
print(a)
b = np.array(["1", 2, 3])       #全て文字列になる
print(b)
c = np.array([True, False, 1.5])    #全てfloatになる
print(c)

#要素の型を指定して配列を作る
a = np.array([1, 1.5, 2], dtype=int)    #整数型で作る
print(a)
b = np.array([1,2,3], dtype=float)      #浮動小数点型で作る
print(b)
c = np.array([1, 1.5, 2], dtype=complex)    #複素数型で作る
print(c)
d = np.array([1, 1.5, 2], dtype="<U")   #文字列型で作る
print(d)
e = np.array([9.123, 10.5, 2.567], dtype="U4")  #最大文字数が4文字になる
print(e)

#配列の型を変換する
a_int = np.array([0,1,2,3,4,5])     
a_float = np.array(a_int, dtype=float)      #要素の型を変換
print(a_float)
