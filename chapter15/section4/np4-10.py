import numpy as np
#カンマ区切りを読み込み、1行目を読み込まない
data = np.loadtxt("chapter15/section4/data.csv", delimiter=",", skiprows=1)
print(data)

import pandas as pd     #pandasモジュール
df = pd.read_csv("chapter15/section4/data.csv")
header = df.columns.values  #ヘッダ行
data = df.values    #データ部分
print(header)
print(data)