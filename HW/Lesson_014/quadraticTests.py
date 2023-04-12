import math


def quadraticEquation(a: int, b: int, c: int):
    """
    Quadratic equation check
    >>> quadraticEquation(2, -5, -4)
    'У уравнения два разных корня: 3.14, -0.64'
    >>> quadraticEquation(4, -2, -8)
    'У уравнения два разных корня: 1.69, -1.19'
    """
    result = ""
    d = b * b - 4 * a * c
    if d < 0:
        result = "У уравнения нет действительных корней"
    elif d == 0:
        x1 = (-b + (math.sqrt(d))) / (2 * a)
        x2 = (-b - (math.sqrt(d))) / (2 * a)
        result = f'У уравнения два равных корня: {x1}, {x2}'
    elif d > 0:
        x1 = (-b + (math.sqrt(d))) / (2 * a)
        x2 = (-b - (math.sqrt(d))) / (2 * a)
        result = f'У уравнения два разных корня: {round(x1,2)}, {round(x2, 2)}'
    return result


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=2)
    # print(quadraticEquation(4, -2, -8))
