#スーパークラス
class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

#サブクラス
class Player(Person):
    def __init__(self, name, age, number, position):
        #スーパークラスの初期化メソッドを呼び出す
        super().__init__(name, age)     #スーパークラスに引数の値を渡す
        self.number = number
        self.position = position

player1 = Player("青木", 16, 10, "MF")  #青木と16はスーパークラスのPersonに渡す
print(player1.name)
print(player1.age)
print(player1.number)
print(player1.position)
