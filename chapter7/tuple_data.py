data = (
    11, 12, 13,
    20, 27,
    34, 35, 39
)
print(data)

data = tuple(range(-5, 6))
print(data)

week = tuple("日月火水木金土")
print(week)

color = ["blue","red", "green", "black"]
data = tuple(color)
print(data)
data = list(data)
print(data)

darui = week[1:4]   #タプルのスライス・・・タプル[開始位置:終了位置:ステップ]（終了位置＝先頭から〇番目）
print(darui)
