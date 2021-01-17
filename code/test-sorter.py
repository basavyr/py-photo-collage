#!/Users/robertpoenaru/.pyenv/shims/python


import matrix_sorter as sort
from numpy import random as rd
import numpy as np

path = '../matrices/sorted_matrices.dat'


def CreateMatrix():
    N = rd.randint(1, 10)
    M = rd.randint(1, 10)
    SIZE = N * M
    mat = np.arange(SIZE).reshape(N, M)
    return mat + 1


F = [CreateMatrix() for _ in range(10)]

with open(path, 'w') as out:
    S = sort.Sorter.Sort(F)
    for x in S:
        out.write(str(x))
        out.write('\n')
