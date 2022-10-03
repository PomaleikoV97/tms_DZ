# 1. sin(x)

k = int(input("Введите точность вычисления "))
x = float(input("Введите угол в градусах "))
x = x * 3.14 / 180
print(x)
p = 1
f = 1
s = x
sine = -1
for i in range(3, k + 1, 2):
    x = x * sine
    p = pow(x, i)
    f = f * i * (i - 1)
    s = s + (p / f)
print('%.2f' % s)


# 2. cos(x)
k = int(input("Введите точность вычисления "))
x = float(input("Введите угол в градусах "))
x = x * 3.14 / 180
print(x)
p = 1
f = 1
s = x
sine = -1
for i in range(2, k + 1, 2):
    x = x * sine
    p = pow(x, i)
    f = f * i
    s = s + (p / f)
print('%.2f' % s)


# 2. Написать filter  с лямбда-функцией определяющей число чётное/нечётное.

from random import randrange
a = [randrange(1, 10) for i in range(20)]
b = list(filter(lambda x: (x % 2 == 0), a))

print(a)
print(b)

# 3. Дан список. Сделать список с помощью функции map, которая переводит каждое число из исходного списка в строку

from random import randrange
a = [randrange(1, 5) for i in range(12)]
b = map(str, a)
print(a)
print(list(b))

# 3. С помощью функции filter отфильтровать из исходного списка строк только те строки, которые являются палиндромами.
# Палиндром - в обе стороны читается одинаково. ‘abccba’ - палиндром например

list_a = ['1221', '222', '32', '555', '4554', '12']
list_b = []
for i in list_a:
    a = i[::-1]
    if a == i:
        list_b.append(a)
print(list_b)

# еще реализации 3 задачи
list_a = ['1221', '222', '32', '555', '4554', '12']
list_b = list(filter(lambda x: x == x[::-1], list_a))
list_c = [i for i in list_a if i == i[::-1]]
print(list_b)
print(list_c)

# Дан словарь, вывести новый словарь, поменяв местами ключи со значениями из исходного словаря
a = {'Haus': 'дом', 'Car': 'машина', 'tree': 'дерево'}
b = dict(zip(a.values(), a.keys()))
print(b)


# Написать функцию для нахождения факториала числа. Две реализации: без рекурсии
n = int(input())
factorial = 1
for i in range(2, n + 1):
    factorial *= i
print(factorial)

# Написать функцию для нахождения факториала числа. Две реализации: через рекурсию

def fac(n):
    if n == 0:
        return 1
    return fac(n - 1) * n


print(fac(5))


# еще задача на циклы: сделать угадайку числа для пользователя.
# Загадываете рандомное число, у юзера 10 попыток.
# У юзера после каждого выигрыша/проигрыша должен быть выбор продолжить игру или нет.
# Если продолжить - рандомите новое число и угадываете снова, если нет - завершаете программу

import random
x = 10
a = random.randint(0, 10)
while x > 0:
    n = input("Input number")
    x -= 1
    if n == a:
        print("You win")
    else:
        print("You playd")
