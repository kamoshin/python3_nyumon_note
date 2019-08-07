import numpy as np
np.random.seed(10)      #ランダムシードを設定する
print(np.random.randn(3))   #乱数を発生
np.random.seed(10)      #同じランダムシードを設定する
print(np.random.randn(3))   #同じ乱数が作られる
