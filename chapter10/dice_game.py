from random import randint

def dice():
    num = randint(1, 6)
    return num

for i in range(5):
    dice1 = dice()
    dice2 = dice()
    dice_sum = dice1 + dice2
    print(f"{dice1}と{dice2}で合計{dice_sum}")