import numpy as np
data = np.loadtxt("chapter15/section4/data.csv", delimiter=",", skiprows=1)
print(data)

import pandas as pd
df = pd.read_csv("chapter15/section4/data.csv")
header = df.columns.values
data = df.values
print(header)
print(data)