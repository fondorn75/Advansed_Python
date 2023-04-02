import math


class Quadratic:

    def quadraticEquation(a: int, b: int, c: int):
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
            result = f'У уравнения два разных корня: {x1}, {x2}'
        return result


if __name__ == '__main__':
    print(Quadratic.quadraticEquation(2, -5, -4))