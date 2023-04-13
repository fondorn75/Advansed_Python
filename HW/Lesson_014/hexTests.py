
def hexCreation(num: int):
    """
    Checks сonverting a number to hexadecimal representation.
    >>> hexCreation(42)
    '0x2a'
    >>> hexCreation(73)
    '0x49'
    """
    return hex(num)


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=2)
    # number = int(input("Введите число: "))
    # print(hexCreation(number))
