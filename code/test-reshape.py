#!/Users/robertpoenaru/.pyenv/shims/python

import numpy as np
import reshape_matrix as mat


N = 4
M = 3

SIZE = N * M

X = mat.Matrix(M, N)


paired_matrix = X.CreatePairIndexMatrix()

for line in paired_matrix:
    print(line)
