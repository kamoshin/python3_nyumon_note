import sys
from datetime import datetime
file = "./data/log.txt"

if len(sys.argv)<2: #1個目の引数はファイル名なので2個以上の時に処理
    sys.exit()      #中断

now = str(datetime.now())   #現在の日時データ
memo = sys.argv[1]          #コマンドライン引数から受け取ったメモ
line = "-" * 10             #区切り線
with open(file, "a", encoding="utf_8") as fileobj:  #追記モードで開く
    fileobj.write(now + "\n")
    fileobj.write(memo + "\n")      #コマンドライン引数で受け取ったメモ
    fileobj.write(line + "\n")