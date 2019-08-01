import numpy as np
a = np.array([0,1,2])
b = np.append(a, 3)     #３を追加する
print(b)
b = np.append(b, [4,5,6])   #同時に３つの値を追加する
print(b)

a = np.array([1,2,3,4,5,6]).reshape(2, 3)   #２行３列の配列にする
print(a)
b = np.append(a, [[7,8,9]], axis = 0)       #配列aに合わせて２次元配列で追加
                                            #axis = 0:新しい行を追加する
print(b)

a = np.array([0,1,2])
b = np.insert(a,1,99)       #配列aのインデックス1の位置に99を挿入
print(b)
b = np.insert(a, 1, [88, 99])   #配列aのインデックス1の位置にリストを挿入
print(b)

words = np.array(["dog", "cat", "bird"])    #文字数の上限はbirdに合わせて4文字になる
new_words = np.insert(words, 0, "snake")    #４文字で区切れてsnakが入る
print(new_words)
new_words = np.delete(words, len(words)-1)  #最期の要素を削除した配列を作る
print(new_words)