import csv
import random
from typing import Callable

_all__ = ["genCsvQuadratic"]


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


@count(10)

def genCsvQuadratic():
    a = random.randint(-10, 10)
    b = random.randint(-10, 10)
    c = random.randint(-10, 10)
    return a, b, c


with open('gencsv.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(genCsvQuadratic())
