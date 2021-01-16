#!/Users/robertpoenaru/.pyenv/shims/python

import reshape_matrix as sh
import numpy as np

N = 5
M = 7

m = sh.Shaper(N, M)

mat = np.arange((N * M)).reshape(N, M) + 1
print(mat)

trunc_mat = m.Truncate(mat, 2, 2)
print(trunc_mat)

ext_mat = m.Extend(mat, 1, 3)
print(ext_mat)
