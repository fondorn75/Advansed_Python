import random


class GeneratorCSV:
    result = ''
    i = 0
    count = 10

    def genCsvQuadratic():

        while GeneratorCSV.i < GeneratorCSV.count:
            a = random.randint(-10, 10)
            b = random.randint(-10, 10)
            c = random.randint(-10, 10)
            GeneratorCSV.result += f'({a}, {b}, {c}) '
            GeneratorCSV.i += 1
        return GeneratorCSV.result


if __name__ == '__main__':
    print(GeneratorCSV.genCsvQuadratic())