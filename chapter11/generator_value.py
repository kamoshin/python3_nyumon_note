def testgen():
    n = 0
    while True:
        received = yield n
        if received:
            n = received
        else:
            n = n + 1

gen = testgen()
print(next(gen))

gen.send(12)
print(next(gen))