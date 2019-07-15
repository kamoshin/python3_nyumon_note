import matplotlib.pyplot as plt
label = ["E", "D", "C", "B", "A"]   #ラベル反時計回り
V = [17, 25, 47, 68, 91]    #値(反時計回り)
ex = [0, 0, 0.1, 0, 0]      #パイの切り出し
plt.pie(V, explode=ex, labels=label, autopct='%1.1f%%', startangle=90)  #円グラフを描く
plt.show()