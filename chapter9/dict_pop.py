#fruit辞書から指定のフルーツを取り出す
fruit = {"apple": 7, "orange": 5, "mango": 3, "peach": 6}
while fruit:        #fruitが空でなければ繰り返す
    key = input("どのフルーツを取り出しますか？(qで終了):")
    if key == "":           #何もタイプされずに入力されたときは続行する
        continue
    elif key == "q":        #qがタイプされたら終了
        print("終了しました。")
        break
    try:
        value = fruit.pop(key)          #keyの値を取り出して要素を削除
        print(f"{key}は{value}個")      #取り出したkeyと値を表示
    except KeyError:                    #入力されなかったキーが辞書になかったらメッセージを表示
        print(f"{key}はありません")
    except Exception as error:
        print(error)
        break
else:                                   #fruitが空になるとループ終了
    print("もう空っぽです")