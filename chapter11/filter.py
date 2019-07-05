#filterで条件に合う要素だけを抜き出す
#filterの使い方：filter(関数, イテラブル)
nums = [4, -3, 9, 1, 5]
nums2 = list(filter(lambda x : x > 0, nums))
nums3 = list(map(lambda x : x > 0, nums))       #mapにするとTrue、Falseがかえってくる
print(nums2)
print(nums3)

#リスト内包表記vera
nums4 = [num for num in nums if num > 0]
print(nums4)