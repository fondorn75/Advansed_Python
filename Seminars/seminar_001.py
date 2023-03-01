import math

# Решите квадратное уравнение 5x2-10x-400=0 последовательно
# сохраняя переменные a, b, c, d, x1 и x2.

result = ""
a = -5
b = 2
c = 8
x1 = 0
x2 = 0
d = b * b - 4 * a * c
if d < 0:
    result = "У уравнения нет действительных корней"
elif d == 0:
    x1 = (-b + (math.sqrt(d))) / (2 * a)
    x2 = (-b - (math.sqrt(d))) / (2 * a)
    result = f'У уравнения два равных корня: {x1}, {x2}'
elif d > 0:
    x1 = (-b + (math.sqrt(d))) / (2 * a)
    x2 = (-b - (math.sqrt(d))) / (2 * a)
    result = f'У уравнения два разных корня: {x1}, {x2}'

print(result)

# Посчитайте сумму чётных элементов от 1 до n исключая
# кратные e.
# Используйте while и if.
# Попробуйте разные значения e и n.

n = 10
e = 4
a = 1
summ = 0
while a < n:
    if a % 2 == 0 and a % e != 0:
        summ += a
    a += 1

print(summ)

# Напишите программу, которая запрашивает год и проверяет его
# на високосность.
# Распишите все возможные проверки в цепочке elif
# откажитесь от магических чисел
# Обязательно учтите год ввода Григорианского календаря
# В коде должны быть один input и один print

userYear = int(input("Введите год: "))
result = ""
if userYear % 4 != 0 or userYear % 100 == 0 and userYear % 400 != 0:
    result = "Обычный год"
else:
    result = "Високосный год"

print(result)

# Пользователь вводит число от 1 до 999. Используя операции с числами
# сообщите что введено: цифра, двузначное число или трёхзначное число.
# Для цифры верните её квадрат, например 5 - 25
# Для двузначного числа произведение цифр, например 30 - 0
# для трёхзначного числа его зеркальное отображение, например 520 - 25
# Если число не из диапазона, запросите новое число
# Откажитесь от магических чисел
# В коде должны быть один input и один print


# Нарисовать в консоли ёлку спросив у пользователя количество рядов.

inputRow = int(input("Введите число рядов: "))
while inputRow > 0:
    print("*")
    inputRow -= 1

# Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.
