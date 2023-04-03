import random


class GeneratorRand:

    def __init__(self):
        self.count = None
        self.i = None
        self.result = None

    def genCsvQuadratic():
        count = 10
        i = 0
        result = ''
        while i < count:
            a = random.randint(-10, 10)
            b = random.randint(-10, 10)
            c = random.randint(-10, 10)
            result += f'({a}, {b}, {c}) '
            i += 1
        return result


if __name__ == '__main__':
    gen = GeneratorRand.genCsvQuadratic()
    print(gen)
