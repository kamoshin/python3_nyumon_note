#数列の値を作るジェネレータ
def num_generator():
    n = 0
    while True:
        num = n*n + 2*n + 3
        yield num
        n += 1

def do_something(num):
    return (num%2, num%3)

gen = num_generator()
for i in range (1, 10):
    num = next(gen)
    result = do_something(num)
    print(result)
