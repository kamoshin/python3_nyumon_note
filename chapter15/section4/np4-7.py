import matplotlib.pyplot as plt
import numpy as np
sigma = 2.5     #分散
mu = 50         #平均
data = sigma * np.random.randn(2, 3) + mu   #正規分布の乱数
print(data)

print(np.random.binomial(n=100, p=0.1, size=(2,3))) #二項分布の乱数
print(np.random.poisson(lam=10, size=(10)))     #ポアソン分布の乱数
