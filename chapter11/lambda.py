#defを使って関数定義した場合
def area(w, h):
    return w * h

num = area(3, 4)
print(num)

#lambda式の場合
#ラムダ式の使い方：lambda 引数1, 引数1, 引数1, 引数n: 実行するステートメント
func = lambda w, h: w * h
#             ↑引数　↑ステートメント
num = func(3, 4)
print(num)