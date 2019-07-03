#クロージャの定義
def charge(price):
    def calc(num):          #専用関数のベースになる関数
        return price * num
    return calc

child = charge(400)     #childのpriceに400を代入している(子供料金の専用関数になった)
adult = charge(1000)    #adultのpriceに1000を代入している(大人料金の専用関数になった)

price1 = child(3)       #子供の専用関数に3人(引数)を渡す
price2 = adult(2)       #大人の専用関数に2人(引数)を渡す
print(price1)
print(price2)