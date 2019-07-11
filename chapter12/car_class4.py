#Carクラス
class Car:
    maker = "PEACE"
    count = 0

    @classmethod
    def countup(cls):
        cls.count += 1
        print(f"出荷台数：{cls.count}")

    def __init__(self, color = "white"):
        Car.countup()
        self.color = color
        self.mynumber = Car.count
        self.mileage = 0

    def drive(self, km):
        self.mileage += km
        msg = f"{km}kmドライブしました。総距離は{self.mileage}です。"
        print(msg)

car1 = Car()
car2 = Car("red")
print(car2.mynumber)