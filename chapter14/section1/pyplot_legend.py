import matplotlib.pyplot as plt
X = [100, 200, 300, 400, 500]
Y1 = [40, 65, 80, 100, 90]
Y2 = [34, 56, 75, 91, 79]
Y3 = [25, 47, 68, 76, 73]
plt.plot(X, Y1, marker = "o", color = "blue", linestyle = "-", label = "Y1")
plt.plot(X, Y2, marker = "v", color = "red", linestyle = "--", label = "Y2")
plt.plot(X, Y3, marker = "^", color = "green", linestyle = "-.", label = "Y3")
plt.legend(loc = "upper left")
plt.show()