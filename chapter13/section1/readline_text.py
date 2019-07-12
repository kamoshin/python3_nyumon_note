file = "./chapter13/data/tsurezuregusa.txt"
with open(file, "r", encoding="utf_8") as fileobj:
    while True:
        line = fileobj.readline()   #1行ずつ読み込む
        aline = line.rstrip()       #改行を取り除く
        if aline:       #文字列があれば出力
            print(aline)
        else:
            break
