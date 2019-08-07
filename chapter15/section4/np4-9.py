import numpy as np
data = np.arange(9).reshape(3, 3)
np.random.shuffle(data)     #並びをシャッフルする
print(data)