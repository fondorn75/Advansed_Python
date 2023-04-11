def hexCreation(number: int):
    return hex(number)


if __name__ == '__main__':
    try:
        number = int(input("Введите число: "))
    except ValueError as e:
        print(f"На вход только числа, а вы ввели - {e}")
        number = 100
        print(f'Будем считать, что вы ввели - {number}')

    print(hexCreation(number))