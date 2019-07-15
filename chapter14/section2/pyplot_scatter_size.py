import matplotlib.pyplot as plt
import numpy as np
X, Y = np.random.rand(100), np.random.rand(100) #ランダムな配列を作る
V = np.random.rand(100)*1000 + 50   #サイズを決めるデータの配列
#sはマーカーのサイズ、cは色、alphaは透明度、linewidthsは線幅、edgecolorsで縁色の指定
plt.scatter(X, Y, s = V, c = "b", alpha = 0.3, linewidths = 1, edgecolors = "b")
plt.show()