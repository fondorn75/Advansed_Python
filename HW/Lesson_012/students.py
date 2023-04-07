# Создайте класс студента.
# Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
# Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы.
# Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
# Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых.

import csv


class Students:

    def __init__(self, name, age, subject, office):
        self.name = name
        self.age = age
        self.subject = subject
        self.office = office

    def __repr__(self):
        return f'Student(Имя = {self.name}, Возраст = {self.age}, Предметы = {self.subject}, Кабинет = {self.office})'

    def readingCsv(self):
        numberList = []
        with open('subjects.csv', 'r', newline='') as f:
            csv_file = csv.reader(f)
            for line in csv_file:
                numberList.append(line)
            return numberList


if __name__ == '__main__':
    s = Students("Иванов Иван Иванович", 18, "subjects", 32)
    subjects = s.readingCsv()
    s.subject = subjects
    print(s.__repr__())

