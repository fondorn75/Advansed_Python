import math


class Quadratic:
    def __init__(self, a: int, b: int, c: int):
        self.a = a
        self.b = b
        self.c = c

    def quadraticEquation(self):
        result = ""
        d = self.b * self.b - 4 * self.a * self.c
        if d < 0:
            result = "У уравнения нет действительных корней"
        elif d == 0:
            x1 = (-self.b + (math.sqrt(d))) / (2 * self.a)
            x2 = (-self.b - (math.sqrt(d))) / (2 * self.a)
            result = f'У уравнения два равных корня: {x1}, {x2}'
        elif d > 0:
            x1 = (-self.b + (math.sqrt(d))) / (2 * self.a)
            x2 = (-self.b - (math.sqrt(d))) / (2 * self.a)
            result = f'У уравнения два разных корня: {x1}, {x2}'
        return result


if __name__ == '__main__':
    try:
        q = Quadratic(2, -5, '-4')
        print(q.quadraticEquation())
    except TypeError as e:
        print(f"Должны передаваться числа - {e}")