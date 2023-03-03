# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

number = int(input("Введите число: "))

result = ""
temp = 0

print(hex(number))

while number != 0:
    temp = number % 16
    number = number // 16
    match temp:
        case 0: result += "0"
        case 1: result += "1"
        case 2: result += "2"
        case 3: result += "3"
        case 4: result += "4"
        case 5: result += "5"
        case 6: result += "6"
        case 7: result += "7"
        case 8: result += "8"
        case 9: result += "9"
        case 10: result += "a"
        case 11: result += "b"
        case 12: result += "c"
        case 13: result += "d"
        case 14: result += "e"
        case 15: result += "f"

result = ''.join(reversed(result))
print(f"0x{result}")

