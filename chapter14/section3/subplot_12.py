import matplotlib.pyplot as plt
X1, Y1 = range(0, 5), [41, 32, 53, 64, 15]
X2, Y2 = range(0, 5), [34, 25, 52, 45, 56]
labels = ["A", "B", "C", "D", "E"]
fig = plt.figure()      #図を作る
ax1 = fig.add_subplot(1, 2, 1)  #サブプロットを追加する(左側)
ax1.bar(X1, Y1, color = "b", tick_label = labels)   #グラフの描画
ax1.set_title("dog")    #グラフのタイトル
ax2 = fig.add_subplot(1, 2, 2)  #サブプロットを追加する(右側)
ax2.bar(X2, Y2, color = "g", tick_label = labels)   #グラフの描画
ax2.set_title("cat")    #グラフのタイトル
plt.show()
