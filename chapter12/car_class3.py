#Carクラス
class Car:
    maker = "PEACE"
    count = 0

    def __init__(self, color = "white"):
        self.color = color
        self.mileage = 0

    def drive(self, km):
        self.mileage += km
        msg = f"{km}kmドライブしました。総距離は{self.mileage}です。"
        print(msg)

print(Car.maker)