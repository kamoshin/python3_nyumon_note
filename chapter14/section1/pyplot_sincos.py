import matplotlib.pyplot as plt
import math
X = range(0, 360)       #x軸の値
S = [math.sin(math.radians(d)) for d in X]  #sinの値
C = [math.cos(math.radians(d)) for d in X]  #cosの値
plt.plot(X, S)      #sinのグラフを描く
plt.plot(X, C)      #cosのグラフを描く
plt.show()