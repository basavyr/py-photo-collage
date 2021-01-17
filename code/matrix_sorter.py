import numpy as np


# used for sorting a list of tuples by specified tuple index
# source: https://stackoverflow.com/questions/10695139/sort-a-list-of-tuples-by-2nd-item-integer-value
# sort by two fields: https://stackoverflow.com/questions/4233476/sort-a-list-by-multiple-attributes
from operator import itemgetter


class Sorter:
    def __init__(self, n_cols, n_rows):
        self.rows = n_rows
        self.cols = n_cols
        self.size = [n_rows, n_cols]
        self.no_elems = n_rows * n_cols

    @staticmethod
    def MatrixInfo(matrix):
        info_tuple = [matrix, len(matrix), len(
            matrix[0]), len(matrix) * len(matrix[0])]
        return info_tuple

    @staticmethod
    def Sort(matrix_list):
        infos = [Sorter.MatrixInfo(mat) for mat in matrix_list]
        sorted_matrices = sorted(infos, key=itemgetter(3, 1, 2), reverse=True)
        return sorted_matrices
