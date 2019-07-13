import matplotlib.pyplot as plt
import math
X = range(0, 360)
Y = [math.sin(math.radians(d)) for d in X]
plt.plot(X, Y)
plt.savefig("./chapter14/section1/sin.png")      #画像ファイルに保存する
plt.show()      #画面表示するならば最後で実行する