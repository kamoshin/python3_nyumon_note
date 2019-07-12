#テキストを読み込んで単語リストを作る
file = "chapter13/data/fox.txt"
with open(file) as fileobj:         #ファイルオブジェクトを作る
    text = fileobj.read()           #ファイルを読み込む
    newtext = text.rstrip(".")      #末尾のピリオドを削除しておく
    wordlist = newtext.split(" ")   #スペースで区切ってリストにする
    print(wordlist)
