#全ての値を順に取り出す
fruit = {"apple": 7, "orange": 5, "mango": 3, "peach": 6}
for key in fruit:
    value = fruit[key]
    print(f"{key}が{value}個")

#辞書のキーをリストにする
print(fruit.keys())          #keyの列挙
keys = list(fruit.keys())    #リストに変換
print(keys)

#キーの一文字目を大文字に変換したリストの作成
keys = [key.capitalize() for key in fruit.keys()]
print(keys)

#辞書の値をリストにする
print(fruit.values())        #valueの列挙
values = list(fruit.values())
print(values)

#辞書の値の合計を調べる
print(sum(fruit.values()))

#辞書のキーとタプルのリストにする
print(fruit.items())
print(list(fruit.items()))

#辞書からキーと値を取り出して出力する
for key, value in fruit.items():
    print(f"{key}が{value}個")