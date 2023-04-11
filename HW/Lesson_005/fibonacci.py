# Создайте функцию генератор чисел Фибоначчи (см. Википедию)

def fibonaci(number: int):
    numberOne = 1
    numberTwo = 1
    result = "0, 1, 1, "
    for i in range(number):
        if i < number:
            sumFib = numberOne + numberTwo
            result += f"{sumFib}, "
            numberOne = numberTwo
            numberTwo = sumFib
            i += 1
            yield result


for i, res in enumerate(fibonaci(12), start=1):
    print(f"{i} = {res}")
