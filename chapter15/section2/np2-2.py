import numpy as np
data = np.array([0,10,20,30,40,50,60,70,80,90])
print(data[:])      #全ての要素(複製)
print(data[:4])     #最初からインデックス番号３まで
print(data[4:])     #インデックス番号４から最後まで
print(data[3:7])    #インデックス番号３からインデックス番号７まで
print(data[::2])    #先頭から１個とび
print(data[::-1])   #末尾から１個ずつ取り出す