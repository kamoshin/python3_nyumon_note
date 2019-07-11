#datetimeモジュール
from datetime import datetime
#Datalogクラス
class Datalog:
    def __init__(self):     #初期化メソッド
        self.loglist = []

    def log(self, data):        #インスタンスメソッド
        now = datetime.now()        #現在の日時データ
        item = (now, data)          #タプルを作る
        self.loglist.append(item)   #loglistに追加する
