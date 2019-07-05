def fizzbuzz():
    n = 1
    while True:
        if n%15 == 0:
            yield "FizzBuzz"
        elif n%3 == 0:
            yield "Fizz"
        elif n%5 == 0:
            yield "Buzz"
        else:
            yield str(n)
        n = n+1

game = fizzbuzz()
for i in range(0, 20):
    print(next(game))