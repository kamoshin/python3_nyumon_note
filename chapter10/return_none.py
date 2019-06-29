def calc(num):
    unit_price = 180
    if not num.isdigit():   #数字がどうかチェックする
        return None         #数字でない時
    price = int(num) * unit_price
    return price

while True:
    num = input("個数を入れて下さい（qで終了）")
    if num == "":
        continue
    elif num == "q":
        break
    result = calc(num)
    print(result)