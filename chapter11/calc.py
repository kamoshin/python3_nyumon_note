#引数と戻り値がある関数オブジェクトを処理する
def calc(func, arg = 1):
    price = func(arg)
    return price

def child(arg):
    return 400 * arg

def adult(arg):
    return 1200 * arg

age = 12
num = 3
if age < 16:                        #16歳未満ならばchild()で計算する
    price = calc(child, num)
else:                               #17歳以上ならばadult()で計算する
    price = calc(adult, num)

print(f"{age}歳、{num}人は{price}円です。")