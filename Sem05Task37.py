# Задача №37.
# Дано натуральное число N и
# последовательность из N элементов.
# Требуется вывести эту последовательность в
# обратном порядке.
# Примечание. В программе запрещается
# объявлять массивы и использовать циклы
# (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3

import random

def massiv(n):
  if n != 0:
    a = str(random.randint(0,9)) # 0
    print(a, end=" ") # 0-5-8-2-8
    return massiv(n - 1) + " " + a # ?-8-2-8-5-0
  return " / "

n = int(input("Введите размерность: "))

print(massiv(n))