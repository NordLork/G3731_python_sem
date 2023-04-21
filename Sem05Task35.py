# Задача №35.
# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes

a = int(input("Введите число: "))
k = 0
for i in range(2, a // 2 + 1):
  if (a % i == 0):
    k = k + 1
if (k <= 0):
  print("Число простое")
else:
  print("Число не является простым")


# n = int(input('Введите число: '))
# for i in range(2, n // 2 + 1):
#   if n % i == 0:
#     print('No')
#     break
#   else:
#     print('Yes')


# def prost(a): #var1
# for i in range(2, int(a**(1 / 2))+1):
# if a % i == 0:
# return "Not prostoe"
# else:
# return "prostoe"

# a = int(input("Введите число: "))
# print(prost(a))


# number = int(input("Введите число: ")) #var2
# i = 2
# def prost(a):
#   while i < number:
#     if number % i == 0:
#       return "Not prostoe"
#     else:
#       return "prostoe"
# print(prost(number))