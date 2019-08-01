import numpy as np
a = np.array([0,1,2,3,4])
b = a[:, np.newaxis]    #配列の次元を上げる
                        #reshape()と違い行列数を知らなくても実行できる
print(b)