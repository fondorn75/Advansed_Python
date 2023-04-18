import argparse
import math


def quadraticEquation(a, b, c):
    d = b * b - 4 * a * c
    if d < 0:
        return 0
    elif d == 0:
        x1 = (-b + (math.sqrt(d))) / (2 * a)
        x2 = (-b - (math.sqrt(d))) / (2 * a)
        return round(x1, 2), round(x2, 2)
    elif d > 0:
        x1 = (-b + (math.sqrt(d))) / (2 * a)
        x2 = (-b - (math.sqrt(d))) / (2 * a)
        return round(x1, 2), round(x2, 2)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Вычисление квадратного уравнения')
    parser.add_argument('param', metavar='a b c', type=int, nargs=3, help='Ввод a b c разделенных пробелом')
    args = parser.parse_args()
    print(quadraticEquation(*args.param))


    