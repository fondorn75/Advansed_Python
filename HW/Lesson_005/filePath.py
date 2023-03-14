# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
import os


def absolutePath():
    fullName = os.path.basename(r'D:\TEMP\Advansed_Python\HW\Lesson_005\HW_5.txt')
    fileName = os.path.splitext(fullName)[0]
    fileExtention = os.path.splitext(fullName)[1]
    pathFile = os.getcwd()
    return pathFile, fileName, fileExtention

print(absolutePath())