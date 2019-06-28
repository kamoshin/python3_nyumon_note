colors = ["blue", "red", "yellow", "red", "green"]
print("削除前", colors)
target = "yellow"
if target in colors:
    colors.remove(target)
print("削除後", colors)