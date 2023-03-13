# Создайте функцию генератор чисел Фибоначчи (см. Википедию)

def fibonacсi(number: int):
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
    return result

print(fibonacсi(12))