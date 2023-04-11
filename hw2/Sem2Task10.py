# Задача 10:
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты
# вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть
# 5 -> 1 0 1 1 0
# 2


# спрашиваем у пользователя количество монет
coins = int(input("Введите колличество монет:"))

kopf = 0  # монетки лежащие орлом
zahl = 0  # монетки лежащие решкой

for i in range(coins):  # спрашиваем у пользователя как лежат монетки
    if int(input(f"{i+1}-я монетка лежит орлом - 0 или решкой - 1? Введите число: ")) == 0:
        kopf = kopf+1
    else:
        zahl = zahl+1
# если орлом лежит меньше монеток, то выводим их количество
if kopf < zahl:
    print(f"Нужно перевернуть {kopf} монет, чтоб все лежали орлом вверх")
else:  # иначе выводим количество монеток лежащих решкой
    print(f"Нужно перевернуть {zahl} монет, чтоб все лежали решкой вверх")


# n = int(input())
# count_zero = 0
# count_one = 0
# for i in range(n):
#     x = int(input())
#     if x == 0:
#         count_zero += 1
#     else:
#         count_one += 1
# if count_one > count_zero:
#     print(count_zero)
# else:
#     print(count_one)
