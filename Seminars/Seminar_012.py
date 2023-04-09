class Range:

    def __init__(self, min_valie: int = None, max_value: int = None):
        self.min_value = min_valie
        self.max_value = max_value

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def __delete__(self, instance):
        raise AttributeError(f'Значение {self.param_name} не может быть удалено.')

    def validate(self, value):
        if not isinstance(value, int):
            raise TypeError(f'Значение {value} должно быть целым числом.')
        if self.min_value is not None and value < self.min_value:
            raise ValueError(f'Значение {value} должно быть меньше {self.min_value}')
        if self.max_value is not None and value >= self.max_value:
            raise ValueError(f'Значение {value} должно быть больше или равно {self.min_value}')


class Student:
    age = Range(3, 103)
    grade = Range(1, 11 + 1)
    office = Range(3, 42 + 1)

    def __init__(self, name, age, grade, office):
        self.name = name
        self.age = age
        self.grade = grade
        self.office = office

    def __repr__(self):
        return f'Student (Name = {self.name}, Age = {self.age}, Grade = {self.grade}, Office = {self.office}'


if __name__ == '__main__':
    s = Student("Иванов", 12, 10, 30)
    print(s.__repr__())
