# Создайте класс Матрица. Добавьте методы для:
# вывода на печать,
# сравнения,
# сложения,
# *умножения матриц


import numpy as np


class Matrix:
    def __init__(self, a1, a2):
        self.a1 = a1
        self.a2 = a2

    def matrixSumm(self):
        """Matrix Addition"""
        return a1 + a2

    def matrixMult(self):
        """Multiplication matrix"""
        return a1.dot(a2)

    def matrixComp(self):
        """Matrix Comparison"""
        return np.array_equiv(a1, a2)

    def printMatrix(self):
        return f'{a1}\n {a2}'


if __name__ == '__main__':
    a1 = np.array([[3, 3, 3], [2, 5, 5], [4, 2, 1]], int)
    a2 = np.array([[2, 5, 4], [5, 3, 2], [6, 4, 3]], int)
    ms = Matrix(a1, a2)
    print(ms.matrixSumm())
    print(ms.matrixMult())

    if not ms.matrixComp():
        print("Матрицы не равны")
    else:
        print('Матрицы равны')

    print(ms.printMatrix())
