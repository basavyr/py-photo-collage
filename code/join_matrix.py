#! /Users/robertpoenaru/.pyenv/shims/python

import numpy as np
from numpy import random as rd


class Joiner:
    def __init__(self, n_rows, n_cols):
        self.cols = n_cols
        self.rows = n_rows
        self.size = [n_rows, n_cols]
        self.no_elems = n_rows * n_cols

    @staticmethod
    def HorizontalJoin(m1, m2):
        size1 = len(m1)
        size2 = len(m2)
        if(size1 != size2):
            print(
                f'Cannot join the two matrices due to unequal sizes: {size1}/{size2}')
            return
        ret_mat = np.append(m1, m2, 1)
        return ret_mat

    @staticmethod
    def VerticalJoin(m1, m2):
        size1 = len(m1[0])
        size2 = len(m2[0])
        if(size1 != size2):
            print(
                f'Cannot join the two matrices due to unequal sizes: {size1}/{size2}')
            return
        ret_mat = np.append(m1, m2, 0)
        return ret_mat
