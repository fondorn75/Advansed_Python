# Напишите функцию, принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ - значение переданного аргумента, а значение - имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.

def argInDictionary(**kwargs):
    result = dict()

    for key, value in kwargs.items():
        result[value] = key
    return result


print(argInDictionary(one=1, two=2, three=3, four=4))
