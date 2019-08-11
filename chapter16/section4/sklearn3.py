from sklearn import datasets
from sklearn import linear_model
import numpy as np
import matplotlib.pyplot as plt
from pandas import DataFrame

boston = datasets.load_boston()     #ボストン市の住宅価格と関連データ
boston_df = DataFrame(boston.data)  #DataFrame型にする
boston_df.columns = boston.feature_names    #列名を設定する
boston_df["Price"] = boston.target      #住宅価格を設定する
print(boston_df[:10])       #最初の10行だけ

#訓練データをつくる
rooms_train = DataFrame(boston_df["RM"])    #部屋数のデータを抜き出す
y_train = boston.target     #ターゲット(住宅価格)
model = linear_model.LinearRegression() #回帰モデルを作る
model.fit(rooms_train, y_train)     #訓練する

#部屋数のテストデータを作る
rooms_test = DataFrame(np.arange(rooms_train.min(), rooms_train.max(), 0.1))
prices_test = model.predict(rooms_test) #モデルを使って住宅価格を予想する

#グラフを表示する(部屋数と住宅価格)
plt.scatter(rooms_train.values.ravel(), y_train, c= "b", alpha= 0.5)    #訓練データ
plt.plot(rooms_test.values.ravel(), prices_test, c= "r")    #回帰直線
plt.title("Boston House Prices dataset")
plt.xlabel("rooms")     #x軸のラベル
plt.ylabel("price $1000's") #y軸のラベル
plt.show()