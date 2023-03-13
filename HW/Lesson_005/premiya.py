# Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
# имена str, ставка int, премия str с указанием процентов вида “10.25%”.
# В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии

def sumPrizes(names: list[str], rates: list[int], prizes: [str]) -> dict[str, float]:
    result = {}
    for name, rate, prize in zip(names, rates, prizes):
        result[name] = (rate * float(prize[:-1])) / 100

    return result


names = ["Иван", "Сергей", "Петр"]
rates = [20000, 25000, 18000]
prizes = ["10.25%", "10.25%", "10.25%"]

print(sumPrizes(names, rates, prizes))
