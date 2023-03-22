# Напишите функцию группового переименования файлов.
# Она должна:
# 1. принимать параметр желаемое конечное имя файлов.
#    При переименовании в конце имени добавляется порядковый номер. +
# 2. принимать параметр количество цифр в порядковом номере. +
# 3. принимать параметр расширение исходного файла.
#    Переименование должно работать только для этих файлов внутри каталога.
# 4. принимать параметр расширение конечного файла.
# 5. принимать диапазон сохраняемого оригинального имени. Например, для диапазона [3, 6] берутся буквы с 3 по 6
#    из исходного имени файла. К ним прибавляется желаемое конечное имя, если оно передано.
#    Далее счётчик файлов и расширение.

# Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.

import os
from pathlib import Path

__all__ = ["sequenceNumber", "userSymbols", "trimName"]


def sequenceNumber(num: int):
    result = ""
    for i in range(num):
        result += "0"
    return result


def userSymbols():
    userSymbol = input("Введите желаемое имя: ")
    return userSymbol


def trimName(name: str, start: int, end: int):
    result = name[start:end]
    return result


if __name__ == "__main__":
    userDir = "D:\\TEMP\\Advansed_Python\\HW\\Lesson_007\\Test\\"
    path = Path(userDir)
    sym = userSymbols()
    for item in path.rglob("*"):
        number = int(sequenceNumber(3)) + 1
        if item.is_file():
            fullName = os.path.basename(item.name)
            fileName = trimName(os.path.splitext(fullName)[0], 2, 5)
            fileExtention = os.path.splitext(fullName)[1]
            result = f"{fileName}{sym}_{number}{fileExtention}"
            os.rename(f"{userDir}{fullName}", f"{userDir}{result}")



