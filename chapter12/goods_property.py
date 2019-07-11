class Goods:
    #初期化メソッド 
    def __init__(self, name, price):
        #非公開の__dataインスタンス変数（辞書）
        self.__data = {"name":name, "price":price}  #プロパティの値は非公開の__data辞書に保存

    #nameプロパティ(ゲッター)
    @property
    def name(self):
        return self.__data["name"]      #__data辞書のnameキーの値を返す

    #nameプロパティ(セッター)
    @name.setter
    def name(self, value):
        self.__data["name"] = value     #__data辞書のnameキーに値を設定する

    @property
    def price(self):
        price = self.__data["price"]    #__data辞書のpriceキーの値を取り出す
        price_str = f"{price:,}円"      #3桁区切りの文字列にして返す
        return price_str

shoes = Goods("dream", 6800)    #shoesを生成
print(shoes.name)       #nameの値を調べる
shoes.name = "瞬足"     #nameの値を更新する
print(shoes.name)
print(shoes.price)      #priceの値を調べる
shoes.price = 7200      #priceを更新しようとするとエラーになる
                        #(priceプロパティにはセッターがなくリードオンリーだから)