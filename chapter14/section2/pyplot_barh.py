import matplotlib.pyplot as plt
labels = ["A", "B", "C", "D", "E"]
y_pos = range(0, 5)
V = [91, 43, 86, 12, 54]
plt.barh(y_pos, V, tick_label = labels)     #横棒グラフを描く
plt.show()