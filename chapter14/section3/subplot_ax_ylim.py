import matplotlib.pyplot as plt
X1, Y1 = range(0, 5), [41, 32, 53, 64, 15]
X2, Y2 = range(0, 5), [17, 12, 26, 22, 28]
labels = ["A", "B", "C", "D", "E"]
fig = plt.figure()
ax1 = fig.add_subplot(1, 2, 1)
ax1.bar(X1, Y1, color = "b", tick_label = labels)
ax1.set_title("dog")
ymin, ymax = plt.ylim()
ax2 = fig.add_subplot(1, 2, 2)
ax2.bar(X2, Y2, color = "g", tick_label = labels)
ax2.set_title("cat")
plt.ylim(ymin, ymax)
plt.show()
