import numpy as np


# Напишите функцию для транспонирования матрицы

def transposeArray():
    newArray = np.array([[3, 5, 8], [4, 2, 7], [1, 3, 9]])
    transArray = newArray.transpose()
    return transArray


print(transposeArray())


def transposeArrayCycle():
    array2 = [[3, 5, 8], [4, 2, 7], [1, 3, 9]]
    transArray = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(len(array2)):
        for j in range(len(array2[0])):
            transArray[j][i] = array2[i][j]
    return transArray

print(transposeArrayCycle())
