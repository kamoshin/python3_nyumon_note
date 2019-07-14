import matplotlib.pyplot as plt
import numpy as np
X, Y = np.random.rand(100), np.random.rand(100)
plt.scatter(X, Y, marker = "o", s = 500, color = "cyan", alpha = 0.5, linewidths = 2, edgecolors = "b")
plt.show()