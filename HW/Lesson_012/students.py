# Создайте класс студента.
# Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
# Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы.
# Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
# Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых.

import csv
import deskRange


class Students:
    age = deskRange.Range(3, 103)
    grade = deskRange.Range(1, 12)
    office = deskRange.Range(3, 43)
    test_result = deskRange.Range(0, 101)

    def __init__(self, name, age, grade, subject, office, testsResult):
        self.name = name
        self.age = age
        self.grade = grade
        self.subject = subject
        self.office = office
        self.testsResult = testsResult
        if not self.name.istitle():
            raise ValueError(f'Значение {self.name} должно быть с заглавной буквы')

    def __repr__(self):
        return f'Student(Имя = {self.name}, ' \
               f'Возраст = {self.age}, ' \
               f'Класс =  {self.grade} ' \
               f'Предметы = {self.subject}, ' \
               f'Кабинет = {self.office}, ' \
               f'Результат теста = {self.testsResult})'

    def readingCsv(self):
        numberList = []
        with open('subjects.csv', 'r', newline='') as f:
            csv_file = csv.reader(f)
            for line in csv_file:
                numberList.append(line)
            return numberList


if __name__ == '__main__':
    s = Students(" Иванов Иван Иванович", 17, 10, "subjects", 32, 98)
    subjects = s.readingCsv()
    s.subject = subjects
    print(s.__repr__())
