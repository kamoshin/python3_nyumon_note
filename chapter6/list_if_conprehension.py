numbers = [2.1, 0.2, 0.3, 1.4, 3.1, 2.4]
result = [num for num in numbers if 1 <= num < 2]
print(result)

numbers = [2.1, "0.2", 0.3, "", 1.4, 3.1, 2.4]
numbers = [num for num in numbers if isinstance(num, (int, float))]
print(numbers)

numbers = [2, 5, 0, 1, 3, 4, 6, 12]
result = [num for num in numbers if num >= 5 if num % 2 == 0]
print(result)

data = [[1,2,3,4], [5,6], [7,8,9]]
result = [num * 2 for alist in data for num in alist]
print(result)

result = [[num*2 for num in alist] for alist in data]
print(result)