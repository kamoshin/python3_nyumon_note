file = "chapter13/data/tsurezuregusa.txt"
target = "心"
with open(file, "r", encoding="utf_8") as fileobj:
    while True:
        try:
            line = next(fileobj)    #イテレータから1行取り出す
            if line.find(target) >=0:   #文字を検索する
                print(f"「{target}」が見つかりました")
                print(line, end = "")
                break
        except StopIteration:       #イテレータの最後まで来たのでブレイク
            print(f"「{target}」は見つかりませんでした")
            break
