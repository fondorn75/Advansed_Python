import random


class GeneratorRand:

    def __init__(self, i, count, result):
        self.count = count
        self.i = i
        self.result = result

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
