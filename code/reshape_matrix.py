#! /Users/robertpoenaru/.pyenv/shims/python

import numpy as np


class Matrix:
    def __init__(self, N_COLS, N_ROWS):
        self.cols = N_COLS
        self.rows = N_ROWS
        self.size = [N_ROWS, N_COLS]

    def CreateMatrix(self):
        m = np.ndarray(shape=(self.rows, self.cols), dtype=int)
        return m

    def ShowMatrix(self):
        print(self.CreateMatrix())
