from sklearn import datasets
from sklearn import svm
from sklearn.model_selection import ShuffleSplit

#アヤメのデータセットを読み込む
iris = datasets.load_iris()
x = iris.data
y = iris.target

#データを分割するインデックスを作る
iris_ss = ShuffleSplit(train_size=0.6, test_size=0.4, random_state=0)
train_index, test_index = next(iris_ss.split(x))

#データを分割する
x_train, y_train = x[train_index], y[train_index]   #訓練データ
x_test, y_test = x[test_index], y[test_index]   #テストデータ
clf = svm.SVC()     #モデルを作る
clf.fit(x_train, y_train)   #訓練する
print(clf.score(x_test, y_test))    #正答率を調べる