import matplotlib.pyplot as plt
price = [200, 300, 400, 500, 600]
count = [31, 29, 25, 28, 26]
plt.plot(price, count)      #グラフを描く
plt.title("count - price")  #タイトル
plt.xlabel("price")     #x軸のラベル
plt.ylabel("count")     #y軸のラベル
plt.show()      #表示する
