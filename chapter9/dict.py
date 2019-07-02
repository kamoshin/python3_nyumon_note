data = dict([("yellow", 3), ("blue", 6), ("green", 5)])
print(data)

keys = ["yellow", "blue", "green"]
values = [3, 4, 5]
data = dict(zip(keys, values))
print(data)
print(data["yellow"])              #辞書型の参照の仕方