
import numpy as np
from numpy import random as rd


class Shaper:
    def __init__(self, n_rows, n_cols):
        self.rows = n_rows
        self.cols = n_cols
        self.no_elems = n_rows * n_cols
        self.size = [n_rows, n_cols]

    @staticmethod
    def AddRows(matrix, n_rows):
        new_matrix = matrix
        new_row = np.array([new_matrix[len(new_matrix)-1]])
        for _ in range(n_rows):
            new_matrix = np.append(new_matrix, new_row, 0)
        return new_matrix

    @staticmethod
    def AddColumns(matrix, n_cols):
        new_column = [[matrix[0, len(matrix[0]) - 1]]
                      for _ in range(len(matrix))]
        new_column = np.array(new_column)
        new_matrix = matrix
        for _ in range(n_cols):
            new_matrix = np.append(new_matrix, new_column, 1)
        return new_matrix

    @ staticmethod
    def RemoveCols(matrix, n_cols):
        new_matrix = matrix
        for _ in range(n_cols):
            new_matrix = np.delete(new_matrix, len(new_matrix[0]) - 1, 1)
        return new_matrix

    @ staticmethod
    def RemoveRows(matrix, n_rows):
        new_matrix = matrix
        for _ in range(n_rows):
            new_matrix = np.delete(new_matrix, len(new_matrix) - 1, 0)
        return new_matrix

    # Method that truncates a given matrix based on the selected number of rows and columns
    @ staticmethod
    def Truncate(matrix, n_rows, n_cols):
        new_matrix = matrix

        # removing the required number of rows
        new_matrix = Shaper.RemoveRows(new_matrix, n_rows)

        # removing the required number of columns
        new_matrix = Shaper.RemoveCols(new_matrix, n_cols)

        return new_matrix

    # Method for extending a given matrix with the selected number of rows and columns
    @ staticmethod
    def Extend(matrix, n_rows, n_cols):
        new_matrix = matrix

        # adds the new columns to the new matrix
        new_matrix = Shaper.AddColumns(new_matrix, n_cols)

        # adds the new rows to the new matrix
        new_matrix = Shaper.AddRows(new_matrix, n_rows)

        return new_matrix
