import matplotlib.pyplot as plt
X = [100, 200, 300, 400, 500]
Y1 = [40, 65, 80, 100, 90]
Y2 = [34, 56, 75, 91, 79]
Y3 = [25, 47, 68, 76, 73]
Y4 = [15, 40, 52, 64, 69]
plt.plot(X, Y1, marker = "o", color = "blue", linestyle = "-")
plt.plot(X, Y2, marker = "v", color = "red", linestyle = "--")
plt.plot(X, Y3, marker = "^", color = "green", linestyle = "-.")
plt.plot(X, Y4, marker = "d", color = "m", linestyle = ":")
plt.show()
