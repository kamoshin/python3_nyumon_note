#スーパークラス
class Greet():
    def hello(self):
        print("やあ")
    
    def bye(self):
        print("さよなら")

#サブクラス
class Greet2(Greet):
    #スーパークラスのメソッドをオーバーライドする
    def hello(self, name = None):
        if name:
            print(name + "さん、こんにちは！")
        else :
            super().hello()     #スーパークラスのhello()をそのまま使う

obj = Greet2()
obj.hello("井上")       #引数があるのでサブクラスのhello()が実行される
obj.hello()             #引数がないのでスーパークラスのhello()が実行される
