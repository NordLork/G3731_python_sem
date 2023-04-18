# Задача 22:
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются
# в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы
# множеств.

mol = [int(x) for x in input().split()]
n = mol[0]
m = mol[1]
set_1 = set()
set_2 = set()
list_1 = list()
a = [int(x) for x in input().split()]
k = set(a)
for i in k:
  set_1.add(i)
b = [int(x) for x in input().split()]
k1 = set(b)
for i in k1:
  set_2.add(i)
lok = set_1 & set_2
kool = list(lok)
kool.sort()
for i in kool:
  print(i, end=' ')


# # спрашиваем у пользователя элементы первого множества
# elements1 = str.split(input("Введите элементы первого множества: "))
# # преобразуем элементы в целые числа и записываем их во множество
# elements1 = set(int(i) for i in elements1)

# elements2 = str.split(input("Введите элементы второго множества: "))
# elements2 = set(int(i) for i in elements2)

# # обьединяем два множества
# uni=elements1.union(elements2)
# # сортируем множество uni и выводим его
# print(sorted(uni))
