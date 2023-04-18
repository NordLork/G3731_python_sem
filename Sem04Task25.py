# Задача №25. Решение в группах
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()

# # Вариант 1
# arr = input('Введите символы через пробел: ').split()
# mn = list(set(arr))
# res = []

# k = [0 for i in range(len(mn))]

# for i in arr:
#   if i not in res:
#     res.append(i)
#   else:
#     for j in range(len(mn)):
#       if i == mn[j]:
#         k[j] += 1
#         res.append(i + "_" + str(k[j]))

# print(*res)


#Вариант 2
arr = input('Введите символы через пробел: ').split()
d = {}

for letter in arr:
  if letter in d:
    print(f'{letter}_{d[letter]}', end=' ')
    # d[letter] += 1
  else:
    print(f'{letter}', end=' ')
    # d[letter] = 1
  d[letter] = d.get(letter, 0) + 1
  