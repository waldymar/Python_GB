import random

class Matrix:

    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.matrix = [[random.randrange(0, 10) for a in range(self.col)] for b in range(self.row)]

    def __str__(self):
        matrix = self.matrix
        for im in range(len(matrix)):
            print(matrix[im])

    def __add__(self, other):
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            raise ValueError('Для сложения размеры матриц должны быть одинаковыми')
        New_Matrix = []
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                New_Matrix.append(self.matrix[i][j] + other.matrix[i][j])
        print(New_Matrix)


m1 = Matrix(3, 4)
m2 = Matrix(3, 4)
m1.__str__()
m2.__str__()
m1.__add__(m2)