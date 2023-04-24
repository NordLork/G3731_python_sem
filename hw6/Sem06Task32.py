# Задача 32: 
# Определить индексы элементов массива (списка), значения которых 
# принадлежат заданному диапазону (т.е. не меньше заданного минимума 
# и не больше заданного максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1,
# 4, -2, 10, 2, 0, -9, 8, 10, -9,
# 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

# elements = str.split(input("Введите элементы массива через пробел:"))
# elements = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
import random
n = int(input('Введите число: '))
elements = [random.randint(-10, 10) for i in range(n)]
print(f"{elements = }")

res=[]
min=int(input("Введите минимум: "))
max=int(input("Введите максимум: "))

for i in range(len(elements)):
    if int(elements[i])>=min and int(elements[i])<=max:
        res.append(i)

print(f"Элементы массива, попадающие в заданный диапазон, имеют индексы: {res}")


# list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# min_number = int(input())
# max_number = int(input())
# for i in range(len(list_1)):
#   if min_number <= list_1[i] <= max_number:
#     print(i)