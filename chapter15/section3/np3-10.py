import matplotlib.pyplot as plt
import numpy as np
X = np.linspace(-np.pi, np.pi, 180)
Y = np.sin(X)
plt.plot(X, Y)
plt.show()