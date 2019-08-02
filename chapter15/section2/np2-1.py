import numpy as np
a = np.array([10, 20, 30, 40, 50])
print(a[0])     #先頭の要素
print(a[1])     #先頭から2番目の要素
print(a[-1])    #最期の要素
a[2] = 99   #インデックス番号2の値を更新
print(a)    #30が99に変更される

data = [10,20,30,40,50,60,70,80,90]
a = np.array(data).reshape(3,3)
print(a[0,0])       #a[0][0]
print(a[1,1])       #a[1][1]
print(a[2,-1])      #a[2][-1]

a = np.array([10,20,30,40])
b = a.reshape(2,2)  #配列aから配列bを作る
print(a is b)   #False(同じオブジェクトではない)
b[0,0] = 99     #配列bの要素を99に書き換える
print(b)
print(a)        #配列bの要素の変更が配列aに影響する