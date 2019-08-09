from sklearn import datasets    #scikit-learnの利用を開始する
from sklearn import svm, metrics
import matplotlib.pyplot as plt

digits = datasets.load_digits()
#手書きの数字データセットを読み込む
x = digits.data     #画像データ
y = digits.target   #教師データ
n_train = len(x)*2//3

x_train, y_train = x[:n_train], y[:n_train] #dataの前半、targetの前半
x_test, y_test = x[n_train:], y[n_train:]   #dataの後半、targetの後半

clf = svm.SVC(gamma=0.001)  #学習器
clf.fit(x_train, y_train)   #訓練データと教師データで学習する

accuracy = clf.score(x_test, y_test)    #テストデータで正答率を調べる
print(f"正答率{accuracy}")
predicted = clf.predict(x_test)     #分類結果を取り出す
n_error = (y_test != predicted).sum()   #正解と分類結果が一致しなかった数の合計
print(f"誤った個数：{n_error}")

print("classification report")
print(metrics.classification_report(y_test, predicted)) #学習結果の評価レポート
print("confusion matrix")
print(metrics.confusion_matrix(y_test, predicted))  #数字ごとに正解数と読み間違えた数字を調べる

#画像イメージと分類結果
imgs_yt_preds = list(zip(digits.images[:n_train], y_test, predicted))   #画像データ、正解、分類結果
for index, (image, y_t, pred) in enumerate(imgs_yt_preds[0:20]):
    plt.subplot(4,5, index + 1)     #4×5で表示
    plt.axis('off')
    plt.tight_layout()
    plt.imshow(image, cmap="Greys", interpolation="nearest")    #画像の表示
    plt.title(f't:{y_t} pre:{pred}', fontsize=12)   #正解と分類結果
plt.show()