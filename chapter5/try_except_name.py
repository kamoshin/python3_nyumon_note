sum =  7600
while True:
    num = input("何人ですか？(qで終了)")
    if num == "q":
        print("終了しました")
        break
    try:
        price = round(sum / int(num))
        if price < 0:
            continue
        print("1人当たりの金額", price)
    except ValueError:
        print("数値を入れて下さい")
    except ZeroDivisionError:
        print("0以外の数値を入れて下さい")