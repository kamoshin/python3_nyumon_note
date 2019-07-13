file = "./chapter13/data/sample.txt"
fileobj = open(file, "w", encoding="utf_8") #1.ファイルを開く(上書きモード)
fileobj.write("こんにちは！\n")     #2.テキストデータを書き込む
fileobj.write("Pythonを始めよう\n") #2.続きを書き込む
fileobj.close()     #ファイルを閉じる

#with-asバージョン
with open(file, "w", encoding="utf_8") as fileobj:
    fileobj.write("こんばんわ\n")
    fileobj.write("Pythonをやろう\n")
        