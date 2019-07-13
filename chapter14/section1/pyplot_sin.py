import matplotlib.pyplot as plt
import math
X = range(0, 360)       #x軸の値
Y = [math.sin(math.radians(d)) for d in X]  #y軸の値
plt.plot(X, Y)      #グラフを描く
plt.show()      #表示する
