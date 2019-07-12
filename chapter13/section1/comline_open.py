import sys
if len(sys.argv) < 2:   #1個目の引数はプログラムファイル名なので2個以上の時に処理
    print("読み込むファイルを選んでください")
    sys.exit()          #プログラム中断

file = sys.argv[1]          #ファイルのパスはargv[1]に入っている
with open(file) as fileobj: #ファイルオブジェクトを作る
    text = fileobj.read()   #ファイルを読み込む
    print(text)