#ソート関数
def size(item):
    sizelist = ["XS", "S", "M", "L"]    #並び順を決める
    pos = sizelist.index(item)          #渡された要素の順位をposに入れる
    return pos

data = ["S", "M", "L", "XS", "XS", "S"]
data.sort(key = size)       #data要素を順番にsizeに渡していく
print(data)

#ラムダver
sizelist = ["XS", "S", "M", "L"]                    #並び順を決める
data = ["S", "M", "L", "XS", "XS", "S"]
data.sort(key = lambda item : sizelist.index(item)) #dataを順に渡し、インデックスを返す
print(data)