def word_quiz(word):
    hint = ""
    for letter in word:
        hint += letter
        yield hint

ans = "Python"
quiz = word_quiz(ans)
while True:
    try:
        hint = next(quiz)
        print(hint)
        word = input("この単語は？")
        if ans.lower() == word.lower():
            point = len(ans) - len(hint)
            print(f"正解です！得点：{point}")
            break
        else:
            print("違います")
    except:
        print("終了です....得点：0")
        break

