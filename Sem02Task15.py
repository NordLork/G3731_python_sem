# 15. Иван Васильевич пришел на рынок и решил
# купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз
# потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество
# арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9
# Output: 1 9


import random
n = int(input('Введите количество арбузов: '))
max, min = 1, 20

for _ in range(n):
  ar = random.randint(1, 20)
  print(ar, end = " ")
  if ar > max:
    max = ar
  elif ar < min:
    min = ar
print("\n",f"Арбуз для себя весит {max} кг, арбуз для тещи весит {min} кг")


# import random
# n = int(input("Введите число арбузов: "))
# minCount = 20
# max_count = 0

# for _ in range(n):
#   val = random.randint(1, 20)
#   print(val, end=" ")
#   if val > max_count:
#     max_count = val
#   elif val < minCount:
#     minCount = val
# print()
# print(minCount, max_count)


# import random
# n = int(input())
# lst = [random.randint(1, 20) for _ in range(n)]
# print(lst, end='')
# print(min(lst),max(lst))
