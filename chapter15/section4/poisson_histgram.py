import numpy as np
import matplotlib.pyplot as plt
#ポアソン分布(平均50、1000個)
data = np.random.poisson(lam=50, size=1000)
count, bins_edges, patches, = plt.hist(data, bins=100)  #ヒストグラム
plt.grid()
plt.show()