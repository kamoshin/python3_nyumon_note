from random import randint
numbers = []
while len(numbers) < 10:
    n = randint(0, 9)
    if n in numbers:
        continue
    numbers.append(n)

print(numbers)