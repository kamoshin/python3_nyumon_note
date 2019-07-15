import matplotlib.pyplot as plt
X1, Y1 = range(0, 7), [41, 32, 53, 64, 15, 23, 68]
X2, Y2 = range(0, 7), [34, 25, 52, 45, 56, 35, 43]
labels = ["A", "B", "C", "D", "E", "F", "G"]
fig = plt.figure()      #図を作る
ax1 = fig.add_subplot(2, 1, 1, facecolor = "cyan")  #サブプロットを追加
ax1.bar(X1, Y1, color = "b", tick_label = labels)   #グラフの描画
ax1.set_title("snake")      #グラフのタイトル
ax2 = fig.add_subplot(2, 1, 2, facecolor = "cyan")  #サブプロットを追加
ax2.bar(X2, Y2, color = "g", tick_label = labels)   #グラフの描画
ax2.set_title("fish")       #グラフのタイトル
plt.tight_layout()      #下図のタイトルが重ならないようにする
plt.show()
