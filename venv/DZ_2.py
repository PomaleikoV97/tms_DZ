import math
# 1
a = 1
a_2 = a ** 2
b = 2
y = (a_2 / 3) + ((a_2 + 4) / b) + (math.sqrt(a_2 + 4) / 4) + (math.sqrt((a_2 + 4) ** 3) / 4)
print(y)

# 2
x = 21
y = math.cos(x) + math.sin(x)
tg_x = (math.sin(2 * x)) / (1 + math.cos(2 * x))
ctg_x = (math.cos(x)) / (math.sin(x))
print(y)
print(tg_x)
print(ctg_x)

# 3
x = 2
y = x ** 5 + x ** 4 + x ** 3 + x ** 2 + x ** 2 + x + 1
print(y)

# 4
from math import cos, sin, sqrt
x = 1
a = 2
b = 3
c = 4
a_y = (0.5 * (x ** 2)) / (a + x)
b_y = (a + b) / (b + ((a + c) / (b + c)))
c_y = (((cos(x ** 2)) ** 2) + ((sin(2 * x - 1)) ** 2)) ** (1./3.)
d_y = (5 * x) + (3 * (x ** 2)) * (math.sqrt(1 + ((sin(x)) ** 2)))


# 5. Играл с кредитами - проиграл
s = int(input("Введите сумму займа: "))
n = int(input("Введите колличество лет на которое взят кредит: "))
p_1 = int(input("Введите ставку по кредиту в процентах: "))
p = p_1 / 100
m = (s * p * ((1 + p) ** n)) / (12 * ((1 + p) ** n) - 1)
overpayment = m * n * 12
print("Ваш ежемесячный платеж составит: " + str('%.2f' % m))
print("Переплата по кредиту составит: " + str('%.2f' % overpayment))



# 6. Задачка на планеты
r_1 = float(input("Введите радиус первой планеты в млн/км: "))
v_1 = float(input("Введите скорость первой планеты в км/ч : "))
p = 3.14
r_2 = float(input("Введите радиус второй планеты в млн/км: "))
v_2 = float(input("Введите скорость второй планеты в км/ч : "))

r_1_1 = r_1 / 1000000
r_2_2 = r_2 / 1000000

year_length_1 = (2 * p * r_1_1) / v_1
year_length_2 = (2 * p * r_2_2) / v_2

if year_length_1 > year_length_2:
    print("На первой планете год длиннее чем на второй")
elif year_length_1 < year_length_2:
    print("На первой планете год короче чем на второй")
else: print("Длинна года на планетах равна!!!")











