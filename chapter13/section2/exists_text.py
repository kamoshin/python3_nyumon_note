import os
from random import randint

#保存フォルダとファイルパス
folder = "./chapter13/data/"
file = folder + "sample.txt"

def filewrite():
    if not os.path.exists(folder):
        os.makedirs(folder)
    with open(file, "w", encoding="utf_8") as fileobj:
        num = randint(0, 100)
        fileobj.write(f"{num}が出ました")
        print("ファイルを保存しました")

if os.path.exists(file):
    while True:
        answer = input("上書きしてもよいですか？(y/n)")
        if answer == "y":
            filewrite()
            break
        elif answer == "n":
            break
else:
    filewrite()