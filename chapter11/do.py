#do()に引数で渡された関数を実行する
def do(func):              #2.引数にthanksかhiが入る
    func()                 #3.引数に入っているメソッドを実行

def thanks():
    print("thank you")

def hi():
    print("hi")

condition = 1
if condition == 1:
    do(thanks)              #1.doにthanksを渡す
else:
    do(hi)