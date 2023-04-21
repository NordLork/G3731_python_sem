# # Задача №29. Решение в группах
# # Ваня и Петя поспорили, кто быстрее решит
# # следующую задачу: “Задана последовательность
# # неотрицательных целых чисел. Требуется определить
# # значение наибольшего элемента
# # последовательности, которая завершается первым
# # встретившимся нулем (число 0 не входит в
# # последовательность)”. Однако 2 друга оказались не
# # такими смышлеными. Никто из ребят не смог до
# # конца сделать это задание. Они решили так: у кого
# # будет меньше ошибок в коде, тот и выиграл спор. За
# # помощью товарищи обратились к Вам, студентам.

# # Ваня:
# n = int(input())
# max_number = 1000
# while n != 0:
#   n = int(input())
#   if max_number > n:
#     max_number = n
# print(max_number)

# # Петя:
# n = int(input())
# max_number = -1
# while n < 0:
#   n = int(input())
#   if max_number < n:
#     n = max_number
# print(n)

# Вариант 1
# n = int(input("Введите число: "))
# max = n
# while n != 0:
#   n = int(input("Введите число: "))
#   if n > max:
#     max = n
# print("Максимальное число: ", max)

# max = 0
# n = -1
# while n != 0:
#   n = int(input("Введите число: "))
#   if n > max:
#     max = n
# print("Максимальное число: ", max)


# Вариант 2
# max = 0
# while w := int(input()):
#   if w > max:
#     max = w
# print(max)

max = 0
while n := int(input("Введите число: ")): # не сравниваем с 0, т.к. while работает пока условие true. 0 = false по умолчанию
  if n > max:
    max = n
print(f'Максимальное число в последовательности: {max}')