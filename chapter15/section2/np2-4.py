import numpy as np
#enumerate()を使って要素を順に取り出す
words = ["flower", "dog", "cat"]
for i, word in enumerate(words):    #配列から要素を取り出す
    print(i, word)      #iには繰り返し回数が入る

#多次元配列の要素を順に取り出す
data = np.array([10,20,30,40,50,60]).reshape(2,3)
for i, item in np.ndenumerate(data):    #多次元配列から位置と要素を取り出す
    print(i, item)      #iには(行、列)のタプルが入る