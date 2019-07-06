def main_gen(n):
    yield "start"
    yield from range(n, 0, -1)
    yield from "abc"
    yield from [10, 20, 30]
    yield from sub_gen()
    yield "end"

def sub_gen():
    yield "X"
    yield "Y"
    yield "Z"

gen = main_gen(3)
print(list(gen))