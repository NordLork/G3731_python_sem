# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.


# import random
# spisok = [random.randint(-10, 10) for i in range(10)]


# import random
# lst = [random.randint(0, 20) for i in range(10)]
# print(lst)
# cnt = 0

# for i in range(len(lst)-1):
#   if lst[i+1] > lst[i]:
#     cnt += 1

# print(cnt)


import random
lst = [random.randint(0, 20) for i in range(10)]
print(lst)
cnt = 0

# for i in range(1, len(lst)):
#   if lst[i] > lst[i-1]:
#     cnt += 1

i = 1
while i < len(lst):
    if lst[i] > lst[i-1]:
        cnt += 1
    i += 1

print(cnt)
