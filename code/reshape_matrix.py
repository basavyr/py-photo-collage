
import numpy as np
from numpy import random as rd


class Shaper:
    def __init__(self, n_rows, n_cols):
        self.rows = n_rows
        self.cols = n_cols
        self.no_elems = n_rows * n_cols
        self.size = [n_rows, n_cols]

    @staticmethod
    def RemoveCols(matrix, n_cols):
        new_matrix = matrix
        for _ in range(n_cols):
            new_matrix = np.delete(new_matrix, len(new_matrix[0]) - 1, 1)
        return new_matrix

    @staticmethod
    def RemoveRows(matrix, n_rows):
        new_matrix = matrix
        for _ in range(n_rows):
            new_matrix = np.delete(new_matrix, len(new_matrix) - 1, 0)
        return new_matrix

    # Method that truncates a given matrix based on the selected number of rows and columns
    @staticmethod
    def Truncate(matrix, n_cols, n_rows):
        new_matrix = matrix

        # removing the required number of rows
        new_matrix = Shaper.RemoveRows(new_matrix, n_rows)

        # removing the required number of columns
        new_matrix = Shaper.RemoveCols(new_matrix, n_cols)

        return new_matrix
