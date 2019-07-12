import tkinter as tk
import tkinter.filedialog as fd
#tkアプリウィンドウを表示しない
root = tk.Tk()
root.withdraw()
#オープンダイアログを表示する
file = fd.askopenfilename(      #fileにはダイアログで選択したファイルのパスが入る
    title = "ファイルを選んでください",
    filetypes = [("TEXT", ".txt"), ("TEXT", ".py"), ("HTML", ".html")]  #ダイアログで選択できるファイルの種類
)

#ファイルが選択されたら開く
if file:    #パスが入っていればTrue
    with open(file, "r", encoding="utf_8") as fileobj:
        text = fileobj.read()
        print(text)