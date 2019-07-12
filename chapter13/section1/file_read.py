file = "./chapter13/data/fox.txt"
fileobj = open(file)    #1.ファイルを開く
text = fileobj.read()   #2.テキストデータを読み込む
fileobj.close()           #3.ファイルを閉じる
print(text)

with open(file) as fileobj:         #ファイルオブジェクトを作る
    text = fileobj.read()           #ファイルを読み込む
    print(text)
