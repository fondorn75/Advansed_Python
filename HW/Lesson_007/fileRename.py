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

__all__ = ["sequenceNumber", "getUserPath", "userFileRename"]


def sequenceNumber(num: int):
    result = ""
    for i in range(num):
        result += "0"
    return result


def getUserPath():
    userDir = "D:\\TEMP\\Advansed_Python\\HW\\Lesson_007\\Test\\"
    result = []
    path = Path(userDir)

    for item in path.rglob("*"):
        if item.is_file():
            result.append(item.name)
    for file in result:
        fullName = os.path.basename(file)
        fileName = os.path.splitext(fullName)[0]
        fileExtention = os.path.splitext(fullName)[1]
        return userDir, fullName, fileName, fileExtention


def userFileRename(newFileName: str, number: int, fileExtension: str):
    result = f"{newFileName}_{number}{fileExtension}"
    os.rename(f"{getUserPath()[0]}{getUserPath()[1]}", f"test/{result}")

    return result


if __name__ == "__main__":
    print(sequenceNumber(3))
    print(getUserPath())
    userFileRename(getUserPath()[2], int(sequenceNumber(3)) + 1, getUserPath()[3])



