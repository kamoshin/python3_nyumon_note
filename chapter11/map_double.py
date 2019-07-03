#map()を使ってリストの数値を2倍にする
def double(x):
    return x * 2

#mapの書式：map(関数, イテラブル)
nums = [4,3,5,6,7,4]
nums2 = list(map(double, nums))      #numsから順番に値を取り出して、doble()で実行した結果をリストにする
print(nums2)

#ラムダ式ver
nums2 = list(map(lambda x : x * 2, nums))
print(nums2)

#リスト内包表記ver
nums2 = [num * 2 for num in nums]
print(nums2)