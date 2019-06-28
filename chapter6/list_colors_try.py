pos = int(input("取り出す位置："))
colors = ["blue", "red", "green", "yellow"]
try:
    item = colors[pos]
    print(item)
except IndexError:
    print("インデックスエラーです")
except Exception as error:
    print(error)
    