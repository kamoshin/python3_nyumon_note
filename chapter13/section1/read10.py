file = "./chapter13/data/fox.txt"
with open(file, "r", encoding="utf_8") as fileobj:
    while True:
        text = fileobj.read(10) #10文字ずつ読み込む
        if text:        #文字列があれば出力
            print(text)
        else:
            break       #読み込み終了
