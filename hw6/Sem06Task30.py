# Задача 30: 
# Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

def MakeProgression(a,d,n):
    list1 =[]
    for i in range(n):
        an = a + (i) * d
        list1.append(an)
    return list1

a = int(input("Введите первый элемент прогрессии: "))
d = int(input("Введите разность: "))
n = int(input("Введите кол-во элементов прогрессии: "))

print(MakeProgression(a, d, n))


# a1 = int(input())
# d = int(input())
# n = int(input())
# print()
# for i in range(n):
#   print(a1 + i * d)
