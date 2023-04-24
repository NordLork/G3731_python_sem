# Задача №43.
# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.
# Ввод:           Вывод:
# 1 2 3 2 3       2

import random
n = int(input('Введите число: '))
lst = [random.randint(-10, 10) for i in range(n)]
print(f"{lst = }")

cnt = 0
i = 0

while slice := lst[i+1:]:
  per = lst[i]
  cnt += slice.count(per)
  i += 1

print(cnt)


# a = [int(b) for b in input().split()]
# count = 0
# for i in range(len(a)): 
#   for c in range(i, len(a) - 1):
#     if a[c] == a[c+1]:
#       count+=1
# print(count)


# cnt = 0
# for i, val in enumerate(lst):
#   slice = lst[i + 1:]
#   if val in slice:
#     cnt += slice.count(val)

# # print(f'{slice = }')
# print(cnt)


# def func(lst):
#   val, *lst = lst # lst = [5, 5, 5, 5, 5] -> val = 5, lst = [5, 5, 5, 5]
#   if lst:
#     return func(lst) + lst.count(val)
#   return 0
