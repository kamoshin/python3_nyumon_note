import numpy as np
a = np.array([3,1,6,4,7,2,9,6,5,2,1,7,8,3,1,3])
a_sort = a.sort()   #配列を並び替えるメソッド
print(a_sort)

b = np.sort([7,2,5,9,6,1,2])    #リストからソート済みの配列を作る
print(b)

a_descend = np.sort(a)[::-1]    #ソートした後で逆順にスライス
print(a_descend)