import random


class GeneratorRand:

    def __init__(self, count, i, result):
        self.count = count
        self.i = i
        self.result = result

    def genCsvQuadratic(self):
        while self.i < self.count:
            a = random.randint(-10, 10)
            b = random.randint(-10, 10)
            c = random.randint(-10, 10)
            self.result += f'({a}, {b}, {c}) '
            self.i += 1
        return self.result


if __name__ == '__main__':
    gen = GeneratorRand(10, 0, '')
    print(gen.genCsvQuadratic())
