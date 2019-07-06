#ジェネレータ式を使う
odd_gen = (odd for odd in range(1, 6, 2))   #外の囲みが()
print(next(odd_gen))
print(next(odd_gen))
print(next(odd_gen))

#ジェネレータをリストに変換して確認する
even_data = (even for even in range(0, 10, 2))
print(list(even_data))