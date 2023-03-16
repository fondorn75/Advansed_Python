# 1. Добавьте в модуль с загадками функцию, которая хранит словарь списков.
# Ключ словаря - загадка, значение - список с отгадками.
# Функция в цикле вызывает загадывающую функцию, чтобы передать ей все свои загадки.
import random

__all__ = ["userRiddles", "dictRiddles"]


def userRiddles(riddle: str, option: list, count: int) -> int:
    print(riddle)
    for i in range(count):
        num = input("Введите ответ: ")
        if num in option:
            return i + 1
    return 0


def dictRiddles() -> dict:
    ridle = {"Зимой и летом одним цветом.": ["Лампочка", "Елка", "Стол", "Курица"],
             "Висит груша нельзя скушать.": ["Лампочка", "Елка", "Стол", "Курица"],
             "У него огромный рот, Он зовется …": ["Бегемот", "Устрица", "Акула", "Мамонт"],
             "По деревьям скок-скок, А орешки щёлк-щёлк.": ["Белка", "Страус", "Курица", "Дятел"]}
    return ridle


if __name__ == '__main__':
    randomRiggle = random.choice(list(dictRiddles()))
    randomAnswer = dictRiddles()[randomRiggle]
    temp = userRiddles(randomRiggle, randomAnswer, 4)
    if temp > 0:
        print(f"Вы угадали с {temp} попытки.")
    else:
        print("Попытки закончились.")
