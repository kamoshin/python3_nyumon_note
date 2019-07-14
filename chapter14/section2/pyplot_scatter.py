import matplotlib.pyplot as plt
from random import randint
X1 = [randint(1, 100) for i in range(20)]   #リストの中に20個の乱数を格納
Y1 = [randint(1, 100) for i in range(20)]   #リストの中に20個の乱数を格納
X2 = [randint(1, 100) for i in range(20)]   #リストの中に20個の乱数を格納
Y2 = [randint(1, 100) for i in range(20)]   #リストの中に20個の乱数を格納
plt.scatter(X1, Y1, marker = "+", color = "red")    #グラフを描く
plt.scatter(X2, Y2, marker = "^", color = "green")  #グラフを描く
plt.show()