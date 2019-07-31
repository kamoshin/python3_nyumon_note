import numpy as np
a = np.array([0,1,2])
b = np.append(a, 3)
print(b)
b = np.append(b, [4,5,6])
print(b)

a = np.array([1,2,3,4,5,6]).reshape(2, 3)
print(a)
b = np.append(a, [[7,8,9]], axis = 0)
print(b)

a = np.array([0,1,2])
b = np.insert(a,1,99)
print(b)

b = np.insert(a, 1, [88, 99])
print(b)

words = np.array(["dog", "cat", "bird"])
new_words = np.insert(words, 0, "snake")
print(new_words)
new_words = np.delete(words, len(words)-1)
print(new_words)