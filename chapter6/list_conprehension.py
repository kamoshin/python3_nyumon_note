#リスト内法表記　[式 for 変数 in イテラブル]
import math

nums = [1,2,3,4,5,6]
nums_double = [num*2 for num in nums]
print(nums_double)

num_list = [5.2, 4.6, 7.7]
result = [math.floor(num) for num in num_list]
print(result)

numbers = [num for num in range(1, 10)]
print(numbers)

group_list = [str+"組" for str in "ABCDEFG"]
print(group_list)

name1 = ["鈴木", "田中", "赤尾", "佐々木", "高田"]
name2 = ["星奈", "実", "恵", "かな", "優"]
longname = [n1 + n2 for n1, n2 in zip (name1, name2)]
print(longname)
