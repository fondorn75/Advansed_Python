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
