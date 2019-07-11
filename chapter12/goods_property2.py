class Goods:
    #初期化メソッド
    def __init__(self, name, price):
        #非公開の__dataインスタンス変数(辞書)
        self.__data = {"name":name, "price":price}

    def get_name(self):
        return self.__data["name"]

    def set_name(self, value):
        self.__data["name"] = value

    def get_price(self):
        price = self.__data["price"]
        price_str = f"{price:,}円"
        return price_str

    name = property(get_name, set_name)
    price = property(get_price)

shoes = Goods("dream", 6800)    #shoesを生成
print(shoes.name)       #nameの値を調べる
shoes.name = "瞬足"     #nameの値を更新する
print(shoes.name)
print(shoes.price)      #priceの値を調べる
