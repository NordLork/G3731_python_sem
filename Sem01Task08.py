# Задача 8:
# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками
# (то есть разломить шоколадку на два прямоугольника).

m = int(input("Введите количество долек шоколадки по горизонтали: "))
n = int(input("Введите количество долек шоколадки по вертикали: "))
k = int(input("Сколько долек нужно отломить: "))

if k % n == 0 or k % m == 0:
    print(f"От шоколадки можно отломить {k} долек")
else:
    print(f"От шоколадки нельзя отломить {k} долек")
