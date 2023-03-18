# 2. Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
# Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне [1, 9999].
# Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
# Проверку года на високосность вынести в отдельную защищённую функцию.
import datetime

__all__ = ["checkDate"]


def checkDate() -> bool:
    try:
        datetime.datetime.strptime(userDate or "", "%d.%m.%Y")
        return True
    except ValueError:
        return False


if __name__ == "__main__":
    userDate = input("Введите дату в формате DD.MM.YYYY: ")
    temp = checkDate()
    if temp:
        print("Дата может существовать")
    else:
        print("Дата не существует. ")
