# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.
# Ввод:               Ввод:
# 5                   5
# 1 2 3 4 5           1 5 1 5 1
# Вывод:              Вывод:
# 0                   2
# (каждое число вводится с новой строки)


# import random
# n = int(input('Введите число: '))
# one = [random.randint(-3, 3) for i in range(n)]
# count = 0
# for i in range(1, n-1):
#   if one[i-1] < one[i] > one[i+1]:
#     count += 1
# print(one)
# print(count)


# a = input('Введите количество элементов\n')
# array = list(map(int, (input('Введите элементы массива через пробел\n')).split()))
# b = len(array)
# c = 0
# print(array)
# for i in range(1, b -1):
#   if (array[i] > array[i-1]) & (array[i] > array[i+1]):
#     c+=1
# print(c)


import random
n = int(input('Введите число: '))
one = [random.randint(-3, 3) for i in range(n)]
p=[one[i-1] < one[i] > one[i+1] for i in range(1, n-1)]
print(p)
count = sum(p)

print(one)
print(count)