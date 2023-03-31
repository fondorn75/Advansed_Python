import csv
from typing import Callable

import decFunc

NUMBER = 10
j = 0


def count(num: int = 1):
    def deco(func: Callable):
        counter = []

        def wrapper(*args, **kwargs):
            for _ in range(num):
                result = func(*args, **kwargs)
                counter.append(result)
            return counter

        return wrapper

    return deco


@count(NUMBER)
def newQuadratic(i=0):
    numberList = []
    with open('gencsv.csv', 'r', newline='') as f:
        csv_file = csv.reader(f)
        for line in csv_file:
            numberList.append(line)
            if i < NUMBER - 2:
                a = numberList[i][j]
                b = numberList[i][j + 1]
                c = numberList[i][j + 2]
            i += 1
        result = a, b, c, decFunc.quadraticEquation(int(a), int(b), int(c))
        print(result)
        return result

newQuadratic()

# with open('newgencsv.csv', 'w', newline='') as f:
#     writer = csv.writer(f)
#     writer.writerows(newQuadratic())
