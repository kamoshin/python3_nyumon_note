from random import randint

def dice():
    num = randint(1, 6)
    return num

def dicegame():
    dice1 = dice()
    dice2 = dice()
    sum = dice1 + dice2
    if sum % 2 == 0:
        print(f"{dice1}と{dice2}で合計{sum}、偶数")
    else:
        print(f"{dice1}と{dice2}で合計{sum}、奇数")

for i in range(5):
    dicegame()
print("終了")