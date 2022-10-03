# 1

a = 1
b = 2
c = 3
print(a + b + c)
print(a - b + c)
print(a * b // c)
print(a * b % c)
print((a ** b / 2) - c * 3)

# 2

import math
a = 3
b = 4
c = math.sqrt(a * a + b * b)
S = (a * b) / 2
print('c = ' + str(c))
print('c = ' + str(math.hypot(a, b)))
print('S = ' + str(S))

# 3

# Формула рассчитана на то, что на входе будут валидные значения, без защиты от дурака.
a = 1
b = 2
l = 3
N = 2

L = ((N - 2) * a) + ((N - 1) * b) + (l * 2)

print(L)

# 4

text = 'Hello World Hello World Hello World'
result = len(text.split())
print("String has " + str(result) + " words.")

substring = "Hello"
result2 = text.count(substring)
print("There are " + str(result2) + " occurrences.")

# 5

text = "Hello"
print(text[2])
print(text[-2])
print(text[0:5])
print(text[0:-2])
print(text[::2])
print(text[1::2])
print(text[::-1])
print(text[::-2])
print(len(text))

# 6

text = "hello hello hello hello hello hello"
a = text.replace("h", "H")
b = a.replace("H", "h", 1)
c = b[::-1]
d = c.replace("H", "h", 1)
f = d[::-1]
print(f)

s = "hello hello hello hello hello hello"
h = "h".join([s.split("h")[0], "H".join(s.split("h")[1:-1]), s.split("h")[-1]])
print(h)

# 7

a = 123
b = a % 10
c = (a // 10 % 10)
print(b)
print(c)

n = int(input("Введите трехзначное число"))
a = n // 100
b = n // 10 % 10
c = n % 10
print(a + b + c)








