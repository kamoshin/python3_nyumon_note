file = "./chapter13/data/numdata.txt"
limit = 2.0
with open(file, "r", encoding="utf_8") as fileobj:
    for i, line in enumerate(fileobj):
        if line == "\n":
            continue        #改行のみスキップ
        datalist = line.split(",")  #リストにする
        #limit以下の時1、大きいとき0に変換する
        result = [int(float(num) <= limit) for num in datalist]
        print(f"{i}:{result}")
        