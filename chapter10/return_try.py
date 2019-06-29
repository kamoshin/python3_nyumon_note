def calc(num):
    unit_price = 180
    try :
        num = float(num)
        return num * unit_price
    except :
        return None

while True:
    num = input("個数を入れて下さい（qで終了）")
    if num == "":
        continue
    elif num == "q":
        break
    result = calc(num)
    print(result)