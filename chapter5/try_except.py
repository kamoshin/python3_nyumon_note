while True:
    num = input("何個ですか？(qで終了)")
    if num == "q":
        print("終了しました")
        break
    try:
        price = 120 * int(num)
        print("金額", price)
    except:
        print("エラーです。正しい値を入力してください")