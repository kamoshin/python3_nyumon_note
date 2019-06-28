#リストに名前が含まれているかどうか判定する
names = ["鈴木裕子", "田中里美", "櫻木翔太"]
name = "里美"
result = False
for item in names:
    if name in item:
        result = True
        break
print(result)