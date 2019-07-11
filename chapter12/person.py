class Person():
    def __init__(self, name):
        self.__name = name      #非公開のインスタンス変数

    def who(self):
        print(self.__name + "です。")   #クラス内では利用できる

man = Person("宇佐美")
man.who()       #インスタンスメソッドを介して__nameの値を調べることはできる
man.__name      #直接アクセスするとエラーになる
