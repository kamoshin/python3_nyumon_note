#Datalogクラスが定義してあるモジュールをインポートする
from datalog import Datalog     #スーパークラスをして指定するためにインポートする
#Datalogクラスを継承したMydataクラス
class Mydata(Datalog):      #Datalogクラスを継承
    def printlog(self):
        for date, data in self.loglist:     #スーパークラスで定義してあるインスタンス変数にアクセス
            print(date, data)

#Mydatakクラスのインスタンス生成
obj = Mydata()
obj.log("あいう")
obj.log("abc")
obj.log(123)
obj.printlog()      #サブクラスのインスタンスメソッドを実行