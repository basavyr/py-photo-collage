import numpy as np
from numpy import random as rd


class Creator:
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
        pairs = [[i + 1, j + 1] for i in range(N + 1) for j in range(M + 1)]

        # create the matrix from the list of pairs
        count = 0
        ret_mat = []
        for id in range(N):
            local_line = []
            for id_2 in range(M):
                local_line.append(pairs[id_2 + count])
            count = count + N
            ret_mat.append(local_line)
        return ret_mat

    def CreatePixelMatrix(self):
        random_pixel = [rd.randint(0, 256), rd.randint(
            0, 256), rd.randint(0, 256)]
        ret_mat = []
        for _ in range(self.rows + 1):
            line = [random_pixel for _ in range(self.cols)]
            ret_mat.append(line)
        return ret_mat

    def PrintMatrix(self):
        print(self.CreateMatrix())
