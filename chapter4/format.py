s = "チューリップは{}と{}と{}でした。"
color = s.format("赤", "青", "黄")
print(color)

name = "高橋"
age = 23
point = 102.5
player = "{}選手、年齢{}、得点{}でした。"
text = player.format(name, age, point)
print(text)

detail = f"{name}選手、年齢{age}、得点{point}でした"
print(detail)