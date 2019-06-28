id_list = ["a1234", "a2345", "a3456", "a4567"]
while True:
    id = input("idを入力してください(qで終了)：")
    if id == "q":
        print("終了しました")
        break
    try:
        pos = id_list.index(id)
        print(str(pos+1) + "番目のメンバーです")
    except:
        print("メンバーではありません")