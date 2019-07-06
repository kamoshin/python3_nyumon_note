#Carクラス
class Car:
    def __init__(self, color = "white"):
        self.color = color      #引数で受け取った値を代入
        self.mileage = 0        #0からスタート

car1 = Car()            #インスタンスcar1の作成
car2 = Car("red")       #インスタンスcar2の作成

#インスタンス変数にアクセスする
#方法：インスタンス.変数名
print(car1.color)
print(car1.mileage)
print(car2.color)

#インスタンス変数colorの値を更新する
car1.color = "green"
print(car1.color)