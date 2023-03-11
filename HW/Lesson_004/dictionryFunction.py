# Напишите функцию, принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ - значение переданного аргумента, а значение - имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.

def argInDictionary(*, userkey=("one", "two", "three", "four")):
    result = dict()

    for key in userkey:
        result[key] = "userkey"
    return result


print(argInDictionary())


def argsDictionary2(**kwargs):
    return kwargs


print(argsDictionary2(a=1, b=2, c=3, d=4))
