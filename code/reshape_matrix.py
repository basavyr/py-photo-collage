#! /Users/robertpoenaru/.pyenv/shims/python

import numpy as np


class Matrix:
    def __init__(self, N_COLS, N_ROWS):
        self.cols = N_COLS
        self.rows = N_ROWS
        self.size = [N_ROWS, N_COLS]
        self.no_elems = N_COLS * N_ROWS

    def LL_CreateMatrix(self):
        m = np.ndarray(shape=(self.rows, self.cols), dtype=int)
        return m

    def ShowMatrix(self, matrix):
        ret_m = matrix
        return ret_m

    def CreatePairIndexMatrix(self):
        N = self.rows
        M = self.cols
        pairs = [[i, j] for i in range(N + 1) for j in range(M + 1)]

        # create the matrix from the list of pairs
        count = 0
        ret_mat = []
        for id in range(M):
            local_line = []
            for id_2 in range(N):
                local_line.append(pairs[id_2 + count])
            count = count + N
            ret_mat.append(local_line)
        return ret_mat

    def PrintMatrix(self):
        print(self.CreateMatrix())
