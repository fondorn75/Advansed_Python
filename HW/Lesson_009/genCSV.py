import csv
import random
from functools import cache


_all__ = ["genCsvQuadratic"]

@cache
def genCsvQuadratic():
    a = random.randint(-10, 10)
    b = random.randint(-10, 10)
    c = random.randint(-10, 10)
    return a, b, c


with open('gencsv.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(genCsvQuadratic())
