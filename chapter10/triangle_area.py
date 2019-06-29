def triangle(base, height):
    area = base * height / 2
    return area

b = 15
h = 13
v = triangle(b, h)
print(f"底辺{b}, 高さ{h}の三角形の面積は{v:.1f}")